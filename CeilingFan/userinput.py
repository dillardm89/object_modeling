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
def modify_fan_input(fan_id):
    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Would you like to modify this fan? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    if choice.upper() == "N":
        selection = -1
        return selection
    else:
        selection = modify_fan_choice(fan_id)
        return selection


# Function to select modification option
def modify_fan_choice(fan_id):
    modify_menu = "What would you like to do?:\n1: Change fan status\n" +\
        "2: Change fan speed\n3: Change fan direction\n4: Return to Main Menu"
    print(modify_menu)

    selection = -1
    valid_input_type = False
    while not valid_input_type or int(selection) < 1 or int(selection) > 4:
        selection = input("Enter the operation number: ")
        valid_input_type = validate_type_is_int(selection)

    return int(selection)


# Function for user input to change status before changing speed/direction
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


# Function for user input to change speed or not
def change_speed_input():
    valid_input_type = False
    speed_choice = ""
    while not valid_input_type or speed_choice.upper() not in ("Y", "N"):
        speed_choice = input("Do you wish to change the speed " +
                             "setting? (Y / N) ")
        valid_input_type = validate_type_is_str(speed_choice)

    return speed_choice.upper()


# Function for user input to change direction or not
def change_direction_input():
    speed_choice = False
    direction_choice = ""
    while not speed_choice or direction_choice.upper() not in ("Y", "N"):
        direction_choice = input("Do you wish to change the direction " +
                                 "setting? (Y / N) ")
        speed_choice = validate_type_is_str(direction_choice)

    return direction_choice.lower()
