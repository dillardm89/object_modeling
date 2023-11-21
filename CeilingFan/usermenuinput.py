from validation import validate_type_is_int


# Function to collect user input for main menu + modify menu (opt 1-6)
def menu_input():
    selection = -1
    valid_input_type = False
    while (valid_input_type is not True or
           int(selection) > 6 or int(selection) < 1):
        selection = input("Enter the operation number: ")
        valid_input_type = validate_type_is_int(selection)

    return int(selection)


# Function to select modification option
def modify_fan_menu():
    modify_menu = "What would you like to do?:\n1: Change fan status\n" +\
        "2: Change fan speed\n3: Change fan direction\n" +\
        "4: Change light status\n5: Change light setting\n" +\
        "6: Return to Main Menu"
    print(modify_menu)

    selection = menu_input()
    return selection
