from validation import validate_type_is_str


# Function for user to input change status or not
def change_status_input(status_type, proposed_status):
    valid_input_type = False
    choice = ""
    while not valid_input_type or choice.upper() not in ("Y", "N"):
        choice = input("Do you wish to turn the " +
                       f"{status_type} {proposed_status} (Y / N) ")
        valid_input_type = validate_type_is_str(choice)

    return choice.upper()


# Function for user input to change fan status before changing speed/direction
def change_fan_status_input(current_fan_status, current_speed,
                            fan_name, change_type):
    if current_fan_status == "on":
        return current_fan_status, current_speed

    print("The fan is currently turned off. " +
          f"It must be on to change the {change_type}.")

    status_type = "fan"
    proposed_status = "on"
    fan_status_choice = change_status_input(status_type, proposed_status)

    if (fan_status_choice == "Y"):
        fan_status = proposed_status
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

    status_type = "light"
    proposed_status = "on"
    light_status_choice = change_status_input(status_type, proposed_status)

    if (light_status_choice == "Y"):
        light_status = proposed_status
        new_light_setting = 1
        print(f"The light for fan named {fan_name} is now turned on")
        return light_status, new_light_setting
    else:
        print(f"The light for fan named {fan_name} will remain off.")
        return current_light_status, current_light_status
