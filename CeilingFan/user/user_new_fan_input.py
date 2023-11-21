from validation import validate_type_is_int


# Function for user input to name fan
def user_name_fan():
    user_fan_string = input("Enter a name for the new fan (ex: bedroom fan): ")

    while user_fan_string[0].isdigit():
        print("The fan name must start with a letter (not a number).")
        user_fan_string = input("Please enter a valid name for the new fan: ")

    return user_fan_string


# Function for user to set number of fan blades
def change_num_blades():
    num_blades = 0
    valid_input_type = False
    while not valid_input_type or int(num_blades) < 3 or int(num_blades) > 6:
        num_blades = input("How many blades does your " +
                           "ceiling fan have? (3-6) ")
        valid_input_type = validate_type_is_int(num_blades)

    return int(num_blades)


# Function for user to set number of fan light bulbs
def change_num_bulbs():
    num_bulbs = 0
    valid_input_type = False
    while not valid_input_type or int(num_bulbs) < 1 or int(num_bulbs) > 5:
        num_bulbs = input("How many light bulbs does your " +
                          "ceiling fan have? (1-5) ")
        valid_input_type = validate_type_is_int(num_bulbs)

    return int(num_bulbs)
