from re import sub
from ceilingfan import CeilingFan

#Createl list for class objects with example fans
myFans = [
    CeilingFan("example fan 123", "exampleFan123", 1, "on", 4, 3, 2, "clockwise"),
    CeilingFan("my bedroom fan", "myBedroomFan", 2, "off", 5, 4),
    CeilingFan("just another fan", "justAnotherFan", 3, "on", 6, 5, 3, "counter-clockwise"),
]


# Function to convert a string to camelCase
def camelCase(userFanString):
    # Use RegEx to replace underscores/hyphens with spaces, then capitalize first letter of words, and remove spaces
    userFanString = sub(r"(_|-)+", " ", userFanString).title().replace(" ", "")
    
    # Join the string and replace first letter with lowercase
    return ''.join([userFanString[0].lower(), userFanString[1:]])
    

#Function to create new class object
def createFan():
    userFanString = input("Enter a name for the new fan (ex: bedroom fan): ")
    
    while userFanString[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        print("The fan name must start with a letter (not a number).")
        userFanString = input("Please enter a valid name for the new fan (ex: upstairs fan): ")
    
    camelFanName = camelCase(userFanString)
    newFan = CeilingFan(userFanString, camelFanName)
    
    myFans.append(newFan)
    newFan.id = myFans.index(newFan) + 1

    print(f"New fan named '{newFan.userName}' has been created.")    


#Function to generate fan list with ID and user inputted name
def createFanList():
    fanIDList = []

    i = 0
    while i < len(myFans):
        fanIDList.append(str(myFans[i].id))
        print(f"{myFans[i].id}: {myFans[i].userName}")
        i += 1
    
    return fanIDList
    
    
#Function to display current fans by ID
def displayFansbyID(selection):
    print("Below is the current fan list.")
    fanIDList = createFanList()
    fanID = selectFanbyID(selection, fanIDList)
    
    return fanID


#Function to select fan by ID
def selectFanbyID(selection, fanIDList):  
    if selection == "2":
        fanID = input("Enter fan ID to delete: ")
    elif selection in ("3", "4"):
        fanID = input("Enter fan ID to view more details: ")
    else:
        fanID = input("Enter fan ID to modify: ")
    
    while fanID not in fanIDList:
        print("Please enter a valid fan ID number.")
        selectFanbyID(selection, fanIDList)
    
    return fanID
    

#Function to delete selected fan by ID
def deleteFan(fanID):
    fanIndexDelete = int(fanID) - 1
    fanNameDelete = myFans[fanIndexDelete].userName
    del myFans[fanIndexDelete]
    
    i = fanIndexDelete
    while i <= len(myFans) -1:
        myFans[i].id -= 1
        i += 1
    
    print(f"Fan named '{fanNameDelete}' has been deleted.")


#Function to view specific fan details by ID
def viewFanDetails(fanID):
    fanIndex = int(fanID) - 1
    print(myFans[fanIndex])

    choice = input("Would you like to modify this fan? (Y / N) ")
    while choice.upper() not in ("Y", "N"):
        print("Please enter a valid selection.")
        choice = input("Would you like to modify this fan? (Y / N) ")
    
    if choice.upper() == "N":
        return
    else:
        modifyFan(fanID)


#Function to modify selected fan by ID
def modifyFan(fanID):  
    fanIndex = int(fanID) - 1
    
    print("What would you like to do?:\n1: Change fan status\n2: Change fan speed\n3: Change fan direction\n4: Return to Main Menu")

    selection = input("Enter the operation number: ")

    while selection not in ("1", "2", "3", "4"):
        print("Please enter a valid number selection.")
        selection = input("Enter a valid operation number: ")
           
    if selection == "1":
        myFans[fanIndex].changeStatus()
        modifyFan(fanID)
    elif selection == "2":
        myFans[fanIndex].changeSpeed()
        modifyFan(fanID)
    elif selection == "3":
        myFans[fanIndex].changeDirection()
        modifyFan(fanID)
    else:
        return