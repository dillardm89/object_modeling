from validation import (validate_type_is_int, validate_type_is_str)
from userinput import (change_fan_status_input, change_setting_input,
                       change_light_status_input)
from usermessage import return_success_msg


# Function for user input to name fan
def user_name_fan():
    user_fan_string = input("Enter a name for the new fan (ex: bedroom fan): ")

    while user_fan_string[0].isdigit():
        print("The fan name must start with a letter (not a number).")
        user_fan_string = input("Please enter a valid name for the new fan: ")

    return user_fan_string


# Function for user to select new fan status
def select_new_fan_status(current_fan_status, current_speed, fan_name):
    print(f"The fan is currently turned {current_fan_status}.")

    if current_fan_status == "off":
        proposed_fan_status = "on"
        proposed_speed = 1
    else:
        proposed_fan_status = "off"
        proposed_speed = 0

    status_choice = ""
    valid_input_type = False
    while not valid_input_type or status_choice.upper() not in ("Y", "N"):
        status_choice = input("Do you wish to turn the fan " +
                              f"{proposed_fan_status}? (Y / N) ")
        valid_input_type = validate_type_is_str(status_choice)

    if status_choice.upper() == "Y":
        new_fan_status = proposed_fan_status
        mode = "Fan"
        action_type = f"turned {proposed_fan_status}"
        return_success_msg(mode, fan_name, action_type)
        return new_fan_status, proposed_speed
    else:
        print(f"Fan named {fan_name} remains turned {current_fan_status}.")
        return current_fan_status, current_speed


# Function for user to select new light status
def select_new_light_status(current_light_status,
                            current_light_setting, fan_name):
    print(f"The light is currently turned {current_light_status}.")

    if current_light_status == "off":
        proposed_light_status = "on"
        proposed_light_setting = 1
    else:
        proposed_light_status = "off"
        proposed_light_setting = 0

    status_choice = ""
    valid_input_type = False
    while not valid_input_type or status_choice.upper() not in ("Y", "N"):
        status_choice = input("Do you wish to turn the light " +
                              f"{proposed_light_status}? (Y / N) ")
        valid_input_type = validate_type_is_str(status_choice)

    if status_choice.upper() == "Y":
        new_light_status = proposed_light_status
        mode = "Light for fan"
        action_type = f"turned {proposed_light_status}"
        return_success_msg(mode, fan_name, action_type)
        return new_light_status, proposed_light_setting
    else:
        print(f"Light for fan named {fan_name} remains " +
              f"turned {current_light_status}.")
        return current_light_status, current_light_setting


# Function for user to select new light setting
def select_new_light_setting(current_light_status,
                             current_light_setting, fan_name):
    details = change_light_status_input(current_light_status,
                                        current_light_setting, fan_name)
    light_status = details[0]
    light_setting = details[1]

    if light_status == "off":
        return current_light_status, current_light_setting

    print(f"The light is currently at setting level {light_setting}.")
    setting_type = "light"
    setting_choice = change_setting_input(setting_type)

    if setting_choice == "N":
        print(f"The light for fan named {fan_name} remains " +
              f"at setting level {light_setting}.")
        return light_status, light_setting

    new_setting = -1
    setting_input_type = False
    while (setting_input_type is not True or
            int(new_setting) < 1 or int(new_setting) > 5):
        new_setting = input("Enter the new light setting: (1-5) ")
        setting_input_type = validate_type_is_int(new_setting)

    if light_setting == int(new_setting):
        print(f"The light is already set to evel {light_setting}.")
        return light_status, light_setting
    else:
        new_setting = int(new_setting)
        mode = "Light for fan"
        action_type = f"changed to speed level {new_setting}"
        return_success_msg(mode, fan_name, action_type)
        return light_status, new_setting


# Function for user to select new speed
def select_new_speed(current_fan_status, current_speed, fan_name):
    change_type = "speed"
    details = change_fan_status_input(current_fan_status,
                                      current_speed, fan_name,
                                      change_type)
    fan_status = details[0]
    speed = details[1]

    if fan_status == "off":
        return current_fan_status, current_speed

    print(f"The fan is currently at speed level {speed}.")
    setting_type = "speed"
    speed_choice = change_setting_input(setting_type)

    if speed_choice == "N":
        print(f"The fan named {fan_name} remains " +
              f"at speed level {speed}.")
        return fan_status, speed

    new_speed = -1
    speed_input_type = False
    while (speed_input_type is not True or
            int(new_speed) < 1 or int(new_speed) > 3):
        new_speed = input("Enter the new speed setting: (1-3) ")
        speed_input_type = validate_type_is_int(new_speed)

    if speed == int(new_speed):
        print(f"The fan is already set to speed level {speed}.")
        return fan_status, speed
    else:
        new_speed = int(new_speed)
        mode = "Fan"
        action_type = f"changed to speed level {new_speed}"
        return_success_msg(mode, fan_name, action_type)
        return fan_status, new_speed


# Function for user to select new direction
def select_new_direction(current_fan_status, current_speed, current_direction,
                         fan_name):
    change_type = "direction"
    details = change_fan_status_input(current_fan_status,
                                      current_speed, fan_name,
                                      change_type)
    fan_status = details[0]
    speed = details[1]

    if fan_status == "off":
        return current_fan_status, current_direction, current_speed

    print(f"The fan is currently set to {current_direction} direction.")
    if (current_direction == "clockwise"):
        print("This is the ideal winter direction setting.")
    else:
        print("This is the ideal summer direction setting.")

    setting_type = "direciton"
    direction_choice = change_setting_input(setting_type)

    if direction_choice == "N":
        print(f"The fan named {fan_name} remains at direction " +
              f"setting: {current_direction}.")
        return fan_status, current_direction, speed

    new_direction = ""
    direction_input_type = False
    while (not direction_input_type or
           new_direction.lower() not in ("clockwise", "counter-clockwise")):
        new_direction = input("Enter the new direction setting: " +
                              "(clockwise or counter-clockwise) ")
        direction_input_type = validate_type_is_str(new_direction)

    if current_direction == new_direction.lower():
        print(f"The fan is already set to {current_direction} direction.")
        return fan_status, current_direction, speed
    else:
        new_direction = new_direction.lower()
        mode = "Fan"
        action_type = f"changed to direction setting: {new_direction}"
        return_success_msg(mode, fan_name, action_type)
        return fan_status, new_direction, speed


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
