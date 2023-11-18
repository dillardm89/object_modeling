import sys
import time
from fanfunctions import create_fan
from fanfunctions import delete_fan
from fanfunctions import update_fan_id
from fanfunctions import view_fan_details
from fanfunctions import create_fan_list
from fanfunctions import MY_FANS
from userfunctions import menu_input
from userfunctions import user_name_fan
from userfunctions import view_details_input
from userfunctions import select_fan_by_id
from userfunctions import modify_fan_input
from userfunctions import modify_fan_choice
from userfunctions import return_success_msg


# Function to create main menu
def main_menu():
    menu_text = "What would you like to do?:\n1: Create new fan\n2: Delete " +\
        "existing fan\n3: View list of fans\n4: View specific fan details\n" +\
        "5: Modify fan (change status, speed, direction)\n6: Exit program"
    print(menu_text)
    selection = menu_input()

    # Create new fan
    if selection == 1:
        fan_name_create = user_name_fan()
        create_fan(fan_name_create)
        action_type = "created"
        return_success_msg(fan_name_create, action_type)
        return_to_menu()

    # Delete existing fan
    elif selection == 2:
        create_fan_list()
        action_type = "delete"
        fan_id = select_fan_by_id(action_type, len(MY_FANS))
        fan_name_delete = delete_fan(fan_id)
        update_fan_id(fan_id)
        return_success_msg(fan_name_delete, f"{action_type}d")
        return_to_menu()

    # View list of fans and/or view specific fan details then option to modify
    elif selection in (3, 4):
        create_fan_list()
        action_type = "view specific details"

        if selection == 3:
            choice = view_details_input()
            if choice == "N":
                return_to_menu()

        fan_id = select_fan_by_id(action_type, len(MY_FANS))
        view_fan_details(fan_id)
        modify_fan_input(fan_id)
        return_to_menu()

    # Modify fan (change status, speed, direction)
    elif selection == 5:
        create_fan_list()
        action_type = "modify"
        fan_id = select_fan_by_id(action_type, len(MY_FANS))
        modify_fan_choice(fan_id)
        return_to_menu()

    # Exit program
    else:
        exit_program()


# Function to return to menu
def return_to_menu():
    input("Press 'Enter' key to return to the main menu.")
    main_menu()


# Function to exit program
def exit_program():
    print("Exiting...")
    time.sleep(1)
    sys.exit()


if __name__ == "__main__":
    main_menu()
