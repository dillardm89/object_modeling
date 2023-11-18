# Function to validate user input type = int
def validate_type_is_int(user_input):
    return isinstance(user_input, int)


# Function to validate user input type = str
def validate_type_is_str(user_input):
    return isinstance(user_input, str)


# Function to collect user input for selecting specific fan
def select_fan_by_id(action_type, fans_len):
    fan_id = -1
    valid_input_type = False
    while (int(fan_id) < 0 or int(fan_id) > fans_len and
           valid_input_type is not True):
        fan_id = input(f"Enter fan ID to {action_type}: ")
        valid_input_type = validate_type_is_int(fan_id)

    return int(fan_id)


# Function to collect user input for main menu
def menu_input():
    selection = -1
    valid_input_type = False
    while (valid_input_type is not True and
           int(selection) > 6 or int(selection) < 1):

        selection = input("Enter the operation number: ")
        valid_input_type = validate_type_is_int(selection)

    return int(selection)


# Function for user input to name fan
def user_name_fan():
    user_fan_string = input("Enter a name for the new fan (ex: bedroom fan): ")

    while user_fan_string[0].isdigit() is True:
        print("The fan name must start with a letter (not a number).")
        user_fan_string = input("Please enter a valid name for the new fan: ")

    return user_fan_string


# Function to collect user input for view fans menu
def view_details_input():
    choice = ""
    valid_input_type = False
    while valid_input_type is not True and choice.upper() not in ("Y", "N"):
        choice = input("Would you like to view details for a " +
                       "specific fan? (Y / N) ")

    return choice


# Function to collect user input for fan details menu
def modify_fan_input():
    choice = ""
    valid_input_type = False
    while valid_input_type is not True and choice.upper() not in ("Y", "N"):
        choice = input("Would you like to modify this fan? (Y / N) ")

    if choice.upper() == "N":
        modify_choice = -1
        return modify_choice
    else:
        modify_choice = modify_fan_choice()
        return modify_choice


# Function to select modification option
def modify_fan_choice():
    modify_menu = "What would you like to do?:\n1: Change fan status\n" +\
        "2: Change fan speed\n3: Change fan direction\n4: Return to Main Menu"
    print(modify_menu)

    selection = -1
    valid_input_type = False
    while (valid_input_type is not True and
           int(selection) < 0 or int(selection) > 4):
        selection = input("Enter the operation number: ")
        valid_input_type = validate_type_is_int(selection)

    return int(selection)


# Function for user input to change status before changing speed/direction
def change_status_input(status, user_name, change_type):
    print("The ceiling fan is currently turned off. " +
          f"It must be on to change the {change_type}.")

    status_choice = ""
    valid_input_type = False
    while (valid_input_type is not True and
            status_choice.upper() not in ("Y", "N")):
        status_choice = input("Do you wish to turn the fan on? (Y / N) ")
        valid_input_type = validate_type_is_str(status_choice)

    if (status_choice.upper() == "Y"):
        status = "on"
        print(f"The fan named {user_name} is now turned on")
        return status
    else:
        print(f"The fan named {user_name} will remain off.")
        return status


# Function for user input to change speed or not
def change_speed_input():
    choice_input_type = False
    choice = ""
    while (choice_input_type is not True and
            choice.upper() not in ("Y", "N")):
        choice = input("Do you wish to change the speed setting? (Y / N) ")
        choice_input_type = validate_type_is_str(choice)

    return choice


# Function for user input to change direction or not
def change_direction_input():
    choice_input_type = False
    choice = ""
    while (choice_input_type is not True and
            choice.upper() not in ("Y", "N")):
        choice = input("Do you wish to change the direction " +
                       "setting? (Y / N) ")
        choice_input_type = validate_type_is_str(choice)

    return choice
