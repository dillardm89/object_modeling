import sys
import time
from fanfunctions import (create_fan, delete_fan, update_fan_id,
                          view_fan_details, create_fan_list,
                          modify_fan, MY_FANS)
from usermessage import return_success_msg
from usernewfaninput import user_name_fan
from usermenuinput import (menu_input, modify_fan_menu)
from useroptioninput import (view_details_input, modify_fan_input)
from userselectactions import select_fan_by_id


# Function to create main menu
def main_menu():
    menu_text = "What would you like to do?:\n1: Create new fan\n2: Delete " +\
        "existing fan\n3: View list of fans\n4: View specific fan details\n" +\
        "5: Modify fan settings\n6: Exit program"
    print(menu_text)
    selection = menu_input()

    # Create new fan
    if selection == 1:
        fan_name_create = user_name_fan()
        create_fan(fan_name_create)
        action_type = "created"
        mode = "Fan"
        return_success_msg(mode, fan_name_create, action_type)
        return_to_menu()

    # Delete existing fan
    elif selection == 2:
        num_fans = create_fan_list()
        if num_fans < 1:
            return_to_menu()

        action_type = "delete"
        fan_id = select_fan_by_id(action_type, len(MY_FANS))
        fan_name_delete = delete_fan(fan_id)
        update_fan_id(fan_id)
        mode = "Fan"
        return_success_msg(mode, fan_name_delete, action_type)
        return_to_menu()

    # View list, view details, or modify
    elif selection in (3, 4, 5):
        num_fans = create_fan_list()
        if num_fans < 1:
            return_to_menu()

        # start point for option 3 = view list all fans
        if selection == 3:
            view_details_choice = view_details_input()
            if view_details_choice == "N":
                return_to_menu()

        if selection in (3, 4):
            action_type = "view specific details"
        else:
            action_type = "modify"

        fan_id = select_fan_by_id(action_type, len(MY_FANS))

        # start point for option 4 = view details specific fan
        if selection in (3, 4):
            view_fan_details(fan_id)
            modify_fan_decision = modify_fan_input()

            if modify_fan_decision == -1:
                return_to_menu()

        # start point for option 5 = modify fan
        modify_choice = -1
        print(modify_choice, type(modify_choice), "before while")
        while modify_choice < 6:
            modify_choice = modify_fan_menu()
            modify_fan(modify_choice, fan_id)

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
