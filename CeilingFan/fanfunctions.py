from ceilingfan import CeilingFan
from userfunctions import select_new_status
from userfunctions import select_new_speed
from userfunctions import select_new_direction

# Create list for class objects with example fans
MY_FANS = [
    CeilingFan(
        "example fan 123", 1, "on", 4, 3, 2, "clockwise"),
    CeilingFan("my bedroom fan", 2, "off", 5, 4),
    CeilingFan(
        "just another fan", 3, "on", 6, 5, 3, "counter-clockwise"),
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
    print("Below is the current fan list.")

    for fan in MY_FANS:
        print(f"{fan.id}: {fan.name}")


# Function to update fan id's after delete performed
def update_fan_id(fan_id):
    i = fan_id - 1
    while i <= len(MY_FANS) - 1:
        MY_FANS[i].id -= 1
        i += 1


# Function to view specific fan details by ID
def view_fan_details(fan_id):
    print(MY_FANS[fan_id - 1])


# Function to modify fan status
def modify_fan_status(fan_id):
    fan_details = MY_FANS[fan_id - 1].get_fan_details
    current_status = fan_details[0]
    fan_name = fan_details[3]

    status = select_new_status(current_status, fan_name)
    MY_FANS[fan_id - 1].change_status(status)


# Function to modify fan speed
def modify_fan_speed(fan_id):
    fan_details = MY_FANS[fan_id - 1].get_fan_details
    current_status = fan_details[0]
    current_speed = fan_details[1]
    fan_name = fan_details[3]

    speed = select_new_speed(current_status, current_speed, fan_name)
    if speed == 0:
        return
    else:
        status = "on"
        MY_FANS[fan_id - 1].change_status(status)
        MY_FANS[fan_id - 1].change_speed(speed)


# Function to modify fan direction
def modify_fan_direction(fan_id):
    selected_fan_details = MY_FANS[fan_id - 1].get_fan_details
    current_status = selected_fan_details[0]
    current_direction = selected_fan_details[2]
    fan_name = selected_fan_details[3]

    direction = select_new_direction(current_status,
                                     current_direction, fan_name)
    if direction is None:
        return
    else:
        status = "on"
        MY_FANS[fan_id - 1].change_status(status)
        MY_FANS[fan_id - 1].change_direction(direction)
