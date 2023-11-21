from validation import (validate_type_is_int, validate_type_is_str)


# Function to collect user input for selecting specific fan
def select_fan_by_id(action_type, fans_len):
    fan_id = -1
    valid_input_type = False
    while not valid_input_type or int(fan_id) < 1 or int(fan_id) > fans_len:
        fan_id = input(f"Enter fan ID to {action_type}: ")
        valid_input_type = validate_type_is_int(fan_id)

    return int(fan_id)


# Function to collect user input for main menu
def menu_input():
    selection = -1
    valid_input_type = False
    while (valid_input_type is not True or
           int(selection) > 6 or int(selection) < 1):
        selection = input("Enter the operation number: ")
        valid_input_type = validate_type_is_int(selection)

    return int(selection)


# Function to collect user input for view fans menu
def view_details_input():
    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Would you like to view details for a " +
                       "specific fan? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()


# Function to collect user input for fan details menu
def modify_fan_input():
    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Would you like to modify this fan? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    if choice.upper() == "N":
        selection = -1
        return selection
    else:
        selection = modify_fan_choice()
        return selection


# Function to select modification option
def modify_fan_choice():
    modify_menu = "What would you like to do?:\n1: Change fan status\n" +\
        "2: Change fan speed\n3: Change fan direction\n" +\
        "4: Change light status\n5: Change light setting\n" +\
        "6: Return to Main Menu"
    print(modify_menu)

    selection = -1
    valid_input_type = False
    while not valid_input_type or int(selection) < 1 or int(selection) > 6:
        selection = input("Enter the operation number: ")
        valid_input_type = validate_type_is_int(selection)

    return int(selection)


# Function for user input to change fan status before changing speed/direction
def change_fan_status_input(current_fan_status, current_speed,
                            fan_name, change_type):
    if current_fan_status == "on":
        return current_fan_status, current_speed

    print("The fan is currently turned off. " +
          f"It must be on to change the {change_type}.")

    fan_status_choice = ""
    valid_input_type = False
    while not valid_input_type or fan_status_choice.upper() not in ("Y", "N"):
        fan_status_choice = input("Do you wish to turn the fan on? (Y / N) ")
        valid_input_type = validate_type_is_str(fan_status_choice)

    if (fan_status_choice.upper() == "Y"):
        fan_status = "on"
        new_speed = 1
        print(f"The fan named {fan_name} is now turned on")
        return fan_status, new_speed
    else:
        print(f"The fan named {fan_name} will remain off.")
        return current_fan_status, current_speed


# Function for user input to change light status before changing setting
def change_light_status_input(current_light_status,
                              current_light_setting, fan_name):
    if current_light_status == "on":
        return current_light_status, current_light_setting

    print("The light is currently turned off. " +
          "It must be on to change the setting.")

    light_status_choice = ""
    valid_input_type = False
    while not valid_input_type or light_status_choice.upper() not in ("Y", "N"):
        light_status_choice = input("Do you wish to turn the light on? (Y / N) ")
        valid_input_type = validate_type_is_str(light_status_choice)

    if (light_status_choice.upper() == "Y"):
        light_status = "on"
        new_light_setting = 1
        print(f"The light for fan named {fan_name} is now turned on")
        return light_status, new_light_setting
    else:
        print(f"The light for fan named {fan_name} will remain off.")
        return current_light_status, current_light_status


# Function for user input to change speed or not
def change_setting_input(setting_type):
    valid_input_type = False
    choice = ""
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input(f"Do you wish to change the {setting_type} " +
                             "setting? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()
