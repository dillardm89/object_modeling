from ceilingfan import CeilingFan

# Create list for class objects with example fans
MY_FANS = [
    CeilingFan(
        "example fan 123", 1, "on", 4, 3, 2, "clockwise"),
    CeilingFan("my bedroom fan", 2, "off", 5, 4),
    CeilingFan(
        "just another fan", 3, "on", 6, 5, 3, "counter-clockwise"),
]
fans_len = len(MY_FANS)


# Function to create new class object
def create_fan(fan_name_create):
    new_fan = CeilingFan(fan_name_create)

    MY_FANS.append(new_fan)
    new_fan.id = MY_FANS.index(new_fan) + 1


# Function to delete selected fan by ID
def delete_fan(fan_id):
    fan_name_delete = MY_FANS[fan_id - 1].user_name
    del MY_FANS[fan_id - 1]

    return fan_name_delete


# Function to generate fan list with ID and user inputted name
def create_fan_list():
    print("Below is the current fan list.")

    for fan in MY_FANS:
        print(f"{fan.id}: {fan.user_name}")


# Function to update fan id's after delete performed
def update_fan_id(fan_id):
    i = fan_id - 1
    while i <= len(MY_FANS) - 1:
        MY_FANS[i].id -= 1
        i += 1


# Function to view specific fan details by ID
def view_fan_details(fan_id):
    print(MY_FANS[fan_id - 1])


# Function to modify selected fan by ID
def modify_fan(selection, fan_id):
    if selection == 1:
        MY_FANS[fan_id - 1].change_status()
    elif selection == 2:
        MY_FANS[fan_id - 1].change_speed()
    elif selection == 3:
        MY_FANS[fan_id - 1].change_direction()
    else:
        return
