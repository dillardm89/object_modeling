from ceilingfan import CeilingFan
from useractions import (select_new_fan_status, select_new_direction,
                         select_new_speed)


# Create list for class objects with example fans
MY_FANS = [
    CeilingFan("example fan 123", 1, "on",
               "off", 4, 3, 2, 0, "clockwise"),
    CeilingFan("my bedroom fan", 2, "off", "on", 5, 4,
               0, 5, "clockwise"),
    CeilingFan("just another fan", 3, "on", "on", 6, 5,
               3, 2, "counter-clockwise"),
    CeilingFan("new on fan", 4, "off", "off", 6, 2,
               0, 0, "clockwise")
]


# Function to create new class object
def create_fan(fan_name_create):
    new_fan = CeilingFan(fan_name_create)

    MY_FANS.append(new_fan)
    new_fan.id = MY_FANS.index(new_fan) + 1


# Function to delete selected fan by ID
def delete_fan(fan_id):
    fan_name_delete = MY_FANS[fan_id - 1].name
    del MY_FANS[fan_id - 1]

    return fan_name_delete


# Function to generate fan list with ID and user inputted name
def create_fan_list():
    if len(MY_FANS) == 0:
        print("There are no fans to view. Try creating new fans first.")
        return -1
    else:
        print("Below is the current fan list.")

        for fan in MY_FANS:
            print(f"{fan.id}: {fan.name}")
        return len(MY_FANS)


# Function to update fan id's after delete performed
def update_fan_id(fan_id):
    i = fan_id - 1
    while i <= len(MY_FANS) - 1:
        MY_FANS[i].id -= 1
        i += 1


# Function to view specific fan details by ID
def view_fan_details(fan_id):
    print(MY_FANS[fan_id - 1])


# Function to handle modify fan options
def modify_fan(selection, fan_id):
    if selection == 1:
        modify_fan_status(fan_id)
    elif selection == 2:
        modify_fan_speed(fan_id)
    else:
        modify_fan_direction(fan_id)


# Function to modify fan status
def modify_fan_status(fan_id):
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_fan_status = fan_details[0]
    current_speed = fan_details[2]
    fan_name = fan_details[5]

    fan_status, speed = select_new_fan_status(current_fan_status,
                                              current_speed, fan_name)
    MY_FANS[fan_id - 1].change_fan_status(fan_status)
    MY_FANS[fan_id - 1].change_speed(speed)


# Function to modify fan speed
def modify_fan_speed(fan_id):
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_fan_status = fan_details[0]
    current_speed = fan_details[2]
    fan_name = fan_details[5]

    speed = select_new_speed(current_fan_status, current_speed, fan_name)
    if speed == 0:
        return
    else:
        fan_status = "on"
        MY_FANS[fan_id - 1].change_fan_status(fan_status)
        MY_FANS[fan_id - 1].change_speed(speed)


# Function to modify fan direction
def modify_fan_direction(fan_id):
    fan_details = MY_FANS[fan_id - 1].get_fan_details()
    current_fan_status = fan_details[0]
    current_speed = fan_details[2]
    current_direction = fan_details[4]
    fan_name = fan_details[5]

    direction, speed = select_new_direction(current_fan_status, current_speed,
                                            current_direction, fan_name)
    if direction is None:
        return
    else:
        fan_status = "on"
        MY_FANS[fan_id - 1].change_fan_status(fan_status)
        MY_FANS[fan_id - 1].change_speed(speed)
        MY_FANS[fan_id - 1].change_direction(direction)
