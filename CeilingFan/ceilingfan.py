# Create a class to model a Ceiling Fan object
class CeilingFan:
    def __init__ (self, userName, camelName, id=None, status="off", blades=None, bulbs=None, speed=1, direction="counter-clockwise"):
        self.userName = userName
        self.camelName = camelName
        self.id = id
        self.status = status.lower()
        self.blades = blades
        self.bulbs = bulbs
        self.speed = speed
        self.direction = direction.lower()
        self.setBlades()
        self.setBulbs()


    #Return string when print(class object) called
    def __str__(self):
        if (self.status == "off"):
            return f"{self.id}: Fan named '{self.userName}' is turned {self.status}. It is equipped with {self.blades} blades and {self.bulbs} light bulbs."
        else:
            return f"{self.id}: Fan named '{self.userName}' is turned {self.status}. It is equipped with {self.blades} blades and {self.bulbs} light bulbs. It is currently moving in {self.direction} direction at speed level {self.speed}."


    #Function to set number of fan blades
    def setBlades(self):
        if (self.blades != None):
            return
        else:
            numBlades = input("How many blades does your ceiling fan have? (3-6) ")

            while numBlades not in ("3", "4", "5", "6"):
                print("Please enter a valid number selection.")
                numBlades = input("How many blades does your ceiling fan have? (3-6) ")

            self.blades = int(numBlades)


    #Function to set number of light bulbs
    def setBulbs(self):
        if (self.bulbs != None):
            return
        else:
            numBulbs = input("How many light bulbs does your ceiling fan have? (1-5) ")

            while numBulbs not in ("1", "2", "3", "4", "5"):
                print("Please enter a valid number selection.")
                numBulbs = input("How many light bulbs does your ceiling fan have? (1-5) ")  
                        
            self.bulbs = int(numBulbs)


    #Function to change fan status (on/off)
    def changeStatus(self):
        oldStatus = self.status
        
        print(f"The fan is currently turned {self.status}.")
        
        if (oldStatus == "off"):
            choice = input("Do you wish to turn the fan on? (Y / N) ")
            while choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                choice = input("Do you wish to turn the fan on? (Y / N) ")

            if (choice.upper() == "Y"):
                self.status = "on"
                print("The fan is now turned on.")
            else:
                print("The fan will remain off.")

        else:
            choice = input("Do you wish to turn the fan off? (Y / N) ")
            while choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                choice = input("Do you wish to turn the fan on? (Y / N) ")

            if (choice.upper() == "Y"):
                self.status = "off"
                print("The fan is now turned off.")
            else:
                print("The fan will remain on.")


    #Function to change fan speed setting (1-3)
    def changeSpeed(self):
        if (self.status == "off"):
            print("The ceiling fan is currently turned off. It must be on to change the speed.")
            statusChoice = input("Do you wish to turn the fan on? (Y / N) ")
            
            while statusChoice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                statusChoice = input("Do you wish to turn the fan on? (Y / N) ")

            if (statusChoice.upper() == "Y"):
                self.status = "on" 
                self.changeSpeed()
            else:
                print("The fan will remain off.")

        else:
            oldSpeed = self.speed
            print(f"The ceiling fan is currently at speed level {self.speed}.")
            choice = input("Do you wish to change the speed setting? (Y / N) ")
            
            while choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                choice = input("Do you wish to change the speed setting? (Y / N) ")
            
            if (choice.upper() == "Y"):
                newSpeed = input("Enter the new speed setting from 1-3: ")
                
                while newSpeed.upper() not in ("1", "2", "3"):
                    print("Please enter a valid number selection.")
                    newSpeed = input("Enter the new speed setting from 1-3: ")

                if (oldSpeed == newSpeed):
                    print(f"The fan is already set to speed level {self.speed}.")
                else:
                    self.speed = int(newSpeed)
                    print(f"The fan is now set to speed level {self.speed}.")
            else:
                print(f"The fan remains at speed level {self.speed}.")


    #Function to change fan direction setting (clockwise / counter-clockwise)
    def changeDirection(self):
        if (self.status == "off"):
            print("The ceiling fan is currently turned off. It must be on to change the direction.")
            directionChoice = input("Do you wish to turn the fan on? (Y / N) ")
            
            while directionChoice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                directionChoice = input("Do you wish to turn the fan on? (Y / N) ")
            
            if (directionChoice.upper() == "Y"):
                self.status = "on" 
                self.changeDirection()
            else:
                print("The fan will remain off.")

        else:
            oldDirection = self.direction
            print(f"The ceiling fan is currently set to {self.direction} direction.")
            
            if (self.direction == "clockwise"):
                print("This is the ideal winter direction setting.")
            else:
                print("This is the ideal summer direction setting.")
            
            choice = input("Do you wish to change the direction setting? (Y / N) ")
            
            while choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                choice = input("Do you wish to change the direction setting? (Y / N) ")
    
            if (choice.upper() == "Y"):
                newDirection = input("Enter the new direction setting: (clockwise or counter-clockwise) ")
                
                while newDirection.lower() not in ("clockwise", "counter-clockwise"):
                    print("Please enter a valid selection.")
                    newDirection = input("Enter the new direction setting: (clockwise or counter-clockwise) ")
                
                self.direction = newDirection.lower()

                if (oldDirection == self.direction):
                    print(f"The fan is already set to {self.direction} direction.")
                else:
                    print(f"The fan is now set to {self.direction} direction.")
            else:
                print(f"The fan will remain set to {self.direction} direction.")
