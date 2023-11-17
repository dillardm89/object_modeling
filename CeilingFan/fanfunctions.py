from ceilingfan import CeilingFan

# Createl list for class objects with example fans
MY_FANS = [
    CeilingFan(
        "example fan 123", 1, "on", 4, 3, 2, "clockwise"),
    CeilingFan("my bedroom fan", 2, "off", 5, 4),
    CeilingFan(
        "just another fan", 3, "on", 6, 5, 3, "counter-clockwise"),
]


# Function to create new class object
def create_fan():
    user_fan_string = input("Enter a name for the new fan (ex: bedroom fan): ")

    while user_fan_string[0] in ("0", "1", "2", "3", "4", "5",
                                 "6", "7", "8", "9"):
        print("The fan name must start with a letter (not a number).")
        user_fan_string = input("Please enter a valid name for the new fan " +
                                "(ex: upstairs fan): ")

    new_fan = CeilingFan(user_fan_string)

    MY_FANS.append(new_fan)
    new_fan.id = MY_FANS.index(new_fan) + 1

    print(f"New fan named '{new_fan.user_name}' has been created.")


# Function to generate fan list with ID and user inputted name
def create_fan_list():
    fan_id_list = []

    for fan in MY_FANS:
        fan_id_list.append(str(fan.id))
        print(f"{fan.id}: {fan.user_name}")

    return fan_id_list


# Function to display current fans by ID
def display_fans_by_id(selection):
    print("Below is the current fan list.")
    fan_id_list = create_fan_list()
    fan_id = select_fan_by_id(selection, fan_id_list)

    return fan_id


# Function to select fan by ID
def select_fan_by_id(selection, fan_id_list):
    fan_id = "-1"
    while fan_id not in fan_id_list:
        if selection == "2":
            fan_id = input("Enter valid fan ID to delete: ")
        elif selection in ("3", "4"):
            fan_id = input("Enter valid fan ID to view more details: ")
        else:
            fan_id = input("Enter valid fan ID to modify: ")

    return fan_id


# Function to delete selected fan by ID
def delete_fan(fan_id):
    fan_index_delete = int(fan_id) - 1
    fan_name_delete = MY_FANS[fan_index_delete].user_name
    del MY_FANS[fan_index_delete]

    i = fan_index_delete
    while i <= len(MY_FANS) - 1:
        MY_FANS[i].id -= 1
        i += 1

    print(f"Fan named '{fan_name_delete}' has been deleted.")


# Function to view specific fan details by ID
def view_fan_details(fan_id):
    fan_index = int(fan_id) - 1
    print(MY_FANS[fan_index])

    choice = input("Would you like to modify this fan? (Y / N) ")
    while choice.upper() not in ("Y", "N"):
        print("Please enter a valid selection.")
        choice = input("Would you like to modify this fan? (Y / N) ")

    if choice.upper() == "N":
        return
    else:
        modify_fan_choice(fan_id)


# Function to select modification option
def modify_fan_choice(fan_id):
    modify_menu = "What would you like to do?:\n1: Change fan status\n" +\
        "2: Change fan speed\n3: Change fan direction\n4: Return to Main Menu"
    print(modify_menu)

    selection = input("Enter the operation number: ")

    while selection not in ("1", "2", "3", "4"):
        print("Please enter a valid number selection.")
        selection = input("Enter a valid operation number: ")

    modify_fan(selection, fan_id)


# Function to modify selected fan by ID
def modify_fan(selection, fan_id):
    fan_index = int(fan_id) - 1

    if selection == "1":
        MY_FANS[fan_index].change_status()
    elif selection == "2":
        MY_FANS[fan_index].change_speed()
    elif selection == "3":
        MY_FANS[fan_index].change_direction()
    else:
        return

    modify_fan_choice(fan_id)
