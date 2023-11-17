import sys
import time
from fanfunctions import create_fan
from fanfunctions import display_fans_by_id
from fanfunctions import delete_fan
from fanfunctions import create_fan_list
from fanfunctions import select_fan_by_id
from fanfunctions import view_fan_details
from fanfunctions import modify_fan_choice


# Function to create main menu
def main_menu():
    menu_text = "What would you like to do?:\n1: Create new fan\n2: Delete " +\
        "existing fan\n3: View list of fans\n4: View specific fan details\n" +\
        "5: Modify fan (change status, speed, direction)\n6: Exit program"
    print(menu_text)

    selection = input("Enter the operation number: ")

    while selection not in ("1", "2", "3", "4", "5", "6"):
        print("Please enter a valid number selection.")
        selection = input("Enter a valid operation number: ")

    # Create new fan
    if selection == "1":
        create_fan()
        return_to_menu()

    # Delete existing fan
    elif selection == "2":
        fan_id = display_fans_by_id(selection)
        delete_fan(fan_id)
        return_to_menu()

    # View list of fans
    elif selection == "3":
        print("Below is the current fan list.")
        fan_id_list = create_fan_list()

        choice = input("Would you like to view details for a " +
                       "specific fan? (Y / N) ")
        while choice.upper() not in ("Y", "N"):
            print("Please enter a valid selection.")
            choice = input("Would you like to view details for a " +
                           "specific fan? (Y / N) ")

        if choice.upper() == "N":
            return_to_menu()
        else:
            fan_id = select_fan_by_id(selection, fan_id_list)
            view_fan_details(fan_id)
            return_to_menu()

    # View specific fan details
    elif selection == "4":
        fan_id = display_fans_by_id(selection)
        view_fan_details(fan_id)
        return_to_menu()

    # Modify fan (change status, speed, direction)
    elif selection == "5":
        fan_id = display_fans_by_id(selection)
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
