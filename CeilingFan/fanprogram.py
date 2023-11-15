import sys, time
from fanfunctions import *


#Function to create main menu
def mainMenu ():
    print("What would you like to do?:\n1: Create new fan\n2: Delete existing fan\n3: View list of fans\n4: View specific fan details\n5: Modify fan (change status, speed, direction)\n6: Exit program")

    selection = input("Enter the operation number: ")

    while selection not in ("1", "2", "3", "4", "5", "6"):
        print("Please enter a valid number selection.")
        selection = input("Enter a valid operation number: ")

    #Create new fan
    if selection == "1":
        createFan()
        return_to_menu()

    #Delete existing fan
    elif selection == "2":
        fanID = displayFansbyID(selection)
        deleteFan(fanID)
        return_to_menu()

    #View list of fans
    elif selection == "3":
        print("Below is the current fan list.")
        fanIDList = createFanList()
        
        choice = input("Would you like to view details for a specific fan? (Y / N) ")
        while choice.upper() not in ("Y", "N"):
            print("Please enter a valid selection.")
            choice = input("Would you like to view details for a specific fan? (Y / N) ")
        
        if choice.upper() == "N":
            return_to_menu()
        else:
            fanID = selectFanbyID(selection, fanIDList)
            viewFanDetails(fanID)
            return_to_menu()

    #View specific fan details
    elif selection == "4":
        fanID = displayFansbyID(selection)
        viewFanDetails(fanID)
        return_to_menu()

    #Modify fan (change status, speed, direction)
    elif selection == "5":
        fanID = displayFansbyID(selection)
        modifyFan(fanID)
        return_to_menu()

    #Exit program
    else:
        exitProgram()


#Function to return to menu
def return_to_menu():
    input("Press 'Enter' key to return to the main menu.")
    mainMenu()
    

#Function to exit program
def exitProgram():
    print("Exiting...")
    time.sleep(1)
    sys.exit()


if __name__ == "__main__":
    mainMenu()