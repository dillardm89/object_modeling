from validation import validate_type_is_int
from validation import validate_type_is_str
from userinput import change_status_input
from userinput import change_speed_input
from userinput import change_direction_input
from usermessage import return_success_msg


# Function for user input to name fan
def user_name_fan():
    user_fan_string = input("Enter a name for the new fan (ex: bedroom fan): ")

    while user_fan_string[0].isdigit():
        print("The fan name must start with a letter (not a number).")
        user_fan_string = input("Please enter a valid name for the new fan: ")

    return user_fan_string


# Function for user to select new status
def select_new_status(current_status, fan_name):
    print(f"The fan is currently turned {current_status}.")

    if current_status == "off":
        proposed_staus = "on"
    else:
        proposed_staus = "off"

    choice = ""
    valid_input_type = False
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Do you wish to turn the fan " +
                       f"{proposed_staus}? (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    if choice.upper() == "Y":
        new_status = proposed_staus
        action_type = f"turned {proposed_staus}"
        return_success_msg(fan_name, action_type)
        return new_status
    else:
        print(f"Fan named {fan_name} remains turned {current_status}.")
        return current_status


# Function for user to select new speed
def select_new_speed(current_status, current_speed, fan_name):
    change_type = "speed"
    status = change_status_input(current_status, fan_name, change_type)

    if status == "off":
        speed = 0
        return speed

    print(f"The fan is currently at speed level {current_speed}.")
    choice = change_speed_input()

    if choice == "N":
        print(f"The fan named {fan_name} remains " +
              f"at speed level {current_speed}.")
        return current_speed

    new_speed = 0
    speed_input_type = False
    while (speed_input_type is not True or
            int(new_speed) < 1 or int(new_speed) > 3):
        new_speed = input("Enter the new speed setting: (1-3) ")
        speed_input_type = validate_type_is_int(new_speed)

    if current_speed == int(new_speed):
        print(f"The fan is already set to speed level {current_speed}.")
        return current_speed
    else:
        new_speed = int(new_speed)
        action_type = f"changed to speed level {new_speed}"
        return_success_msg(fan_name, action_type)
        return new_speed


# Function for user to select new direction
def select_new_direction(current_status, current_direction, fan_name):
    change_type = "direction"
    status = change_status_input(current_status, fan_name, change_type)

    if status == "off":
        direction = None
        return direction

    print(f"The fan is currently set to {current_direction} direction.")
    if (current_direction == "clockwise"):
        print("This is the ideal winter direction setting.")
    else:
        print("This is the ideal summer direction setting.")

    choice = change_direction_input()

    if choice == "N":
        print(f"The fan named {fan_name} remains at direction " +
              f"setting: {current_direction}.")
        return current_direction

    new_direction = ""
    direction_input_type = False
    while (not direction_input_type or
           new_direction.lower() not in ("clockwise", "counter-clockwise")):
        new_direction = input("Enter the new direction setting: " +
                              "(clockwise or counter-clockwise) ")
        direction_input_type = validate_type_is_str(new_direction)

    if current_direction == new_direction.lower():
        print(f"The fan is already set to {current_direction} direction.")
        return current_direction
    else:
        new_direction = new_direction.lower()
        action_type = f"changed to direction setting: {new_direction}"
        return_success_msg(fan_name, action_type)
        return new_direction


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
