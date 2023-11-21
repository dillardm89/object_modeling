from validation import validate_type_is_int
from useroptioninput import (change_setting_input, new_light_setting_input,
                             new_speed_setting_input,
                             new_direction_setting_input)
from userstatusinput import (change_fan_status_input, change_status_input,
                             change_light_status_input)
from usermessage import return_success_msg


# Function to collect user input for selecting specific fan
def select_fan_by_id(action_type, fans_len):
    fan_id = -1
    valid_input_type = False
    while not valid_input_type or int(fan_id) < 1 or int(fan_id) > fans_len:
        fan_id = input(f"Enter fan ID to {action_type}: ")
        valid_input_type = validate_type_is_int(fan_id)

    return int(fan_id)


# Function for user to select new fan status
def select_new_fan_status(current_fan_status, current_speed, fan_name):
    print(f"The fan is currently turned {current_fan_status}.")

    if current_fan_status == "off":
        proposed_fan_status = "on"
        proposed_speed = 1
    else:
        proposed_fan_status = "off"
        proposed_speed = 0

    status_type = "fan"
    status_choice = change_status_input(status_type, proposed_fan_status)

    if status_choice == "Y":
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

    status_type = "light"
    status_choice = change_status_input(status_type, proposed_light_status)

    if status_choice == "Y":
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

    light_setting_choice = new_light_setting_input()
    if light_setting == light_setting_choice:
        print(f"The light is already set to evel {light_setting}.")
        return light_status, light_setting
    else:
        new_setting = light_setting_choice
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

    new_speed_choice = new_speed_setting_input()
    if speed == int(new_speed_choice):
        print(f"The fan is already set to speed level {speed}.")
        return fan_status, speed
    else:
        new_speed = int(new_speed_choice)
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

    new_direction_choice = new_direction_setting_input()
    if current_direction == new_direction_choice:
        print(f"The fan is already set to {current_direction} direction.")
        return fan_status, current_direction, speed
    else:
        new_direction = new_direction_choice
        mode = "Fan"
        action_type = f"changed to direction setting: {new_direction}"
        return_success_msg(mode, fan_name, action_type)
        return fan_status, new_direction, speed
