from validation import (validate_type_is_int, validate_type_is_str)
from usermenuinput import modify_fan_menu


# Function to collect user input for view fans menu
def view_details_input():
    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Would you like to view details for a " +
                       "specific fan? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()


# Function for user input to change speed or not
def change_setting_input(setting_type):
    valid_input_type = False
    choice = ""
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input(f"Do you wish to change the {setting_type} " +
                       "setting? (Y / N) ")
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
        selection = modify_fan_menu()
        return selection


# Function to collect user input for light setting
def new_light_setting_input():
    new_setting_choice = -1
    setting_input_type = False
    while (setting_input_type is not True or
            int(new_setting_choice) < 1 or int(new_setting_choice) > 5):
        new_setting_choice = input("Enter the new light setting: (1-5) ")
        setting_input_type = validate_type_is_int(new_setting_choice)

    return int(new_setting_choice)


# Function to collect user input for speed setting
def new_speed_setting_input():
    new_speed_choice = -1
    speed_input_type = False
    while (speed_input_type is not True or
            int(new_speed_choice) < 1 or int(new_speed_choice) > 3):
        new_speed_choice = input("Enter the new speed setting: (1-3) ")
        speed_input_type = validate_type_is_int(new_speed_choice)

    return int(new_speed_choice)


# Function to collect user input for direction setting
def new_direction_setting_input():
    new_direction_choice = ""
    direction_input_type = False
    while (not direction_input_type or
           new_direction_choice.lower() not in ("clockwise", "counter-clockwise")):
        new_direction_choice = input("Enter the new direction setting: " +
                                     "(clockwise or counter-clockwise) ")
        direction_input_type = validate_type_is_str(new_direction_choice)

    return new_direction_choice.lower()
