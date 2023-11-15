# Create a class to model a Ceiling Fan object
class CeilingFan:
    def __init__(
        self, user_name, id=None, status="off", blades=None,
            bulbs=None, speed=1, direction="counter-clockwise"):

        self.user_name = user_name
        self.id = id
        self.status = status.lower()
        self.blades = blades
        self.bulbs = bulbs
        self.speed = speed
        self.direction = direction.lower()
        self.set_blades()
        self.set_bulbs()

    # Return string when print(class object) called
    def __str__(self):
        if (self.status == "off"):
            return f"{self.id}: Fan named '{self.user_name}' is turned " +\
                f"{self.status}. It is equipped with {self.blades} blades " +\
                f"and {self.bulbs} light bulbs."
        else:
            return f"{self.id}: Fan named '{self.user_name}' is turned " +\
                f"{self.status}. It is equipped with {self.blades} blades " +\
                f"and {self.bulbs} light bulbs. It is currently moving in " +\
                f"{self.direction} direction at speed level {self.speed}."

    # Function to set number of fan blades
    def set_blades(self):
        if self.blades is None:
            numBlades = input("How many blades does your ceiling fan have? (3-6) ")

            while numBlades not in ("3", "4", "5", "6"):
                print("Please enter a valid number selection.")
                numBlades = input("How many blades does your ceiling fan have? (3-6) ")

            self.blades = int(numBlades)
        else:
            return

    # Function to set number of light bulbs
    def set_bulbs(self):
        if self.bulbs is None:
            numBulbs = input("How many light bulbs does your ceiling fan have? (1-5) ")

            while numBulbs not in ("1", "2", "3", "4", "5"):
                print("Please enter a valid number selection.")
                numBulbs = input("How many light bulbs does your ceiling fan have? (1-5) ")

            self.bulbs = int(numBulbs)
        else:
            return

    # Function to change fan status (on/off)
    def change_status(self):
        old_status = self.status

        print(f"The fan is currently turned {self.status}.")

        if (old_status == "off"):
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

    # Function to change fan speed setting (1-3)
    def change_speed(self):
        if (self.status == "off"):
            print("The ceiling fan is currently turned off. It must be on to change the speed.")
            status_choice = input("Do you wish to turn the fan on? (Y / N) ")

            while status_choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                status_choice = input("Do you wish to turn the fan on? (Y / N) ")

            if (status_choice.upper() == "Y"):
                self.status = "on"
                self.change_speed()
            else:
                print("The fan will remain off.")

        else:
            old_speed = self.speed
            print(f"The ceiling fan is currently at speed level {self.speed}.")
            choice = input("Do you wish to change the speed setting? (Y / N) ")

            while choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                choice = input("Do you wish to change the speed setting? (Y / N) ")

            if (choice.upper() == "Y"):
                new_speed = input("Enter the new speed setting from 1-3: ")

                while new_speed.upper() not in ("1", "2", "3"):
                    print("Please enter a valid number selection.")
                    new_speed = input("Enter the new speed setting from 1-3: ")

                if (old_speed == new_speed):
                    print(f"The fan is already set to speed level {self.speed}.")
                else:
                    self.speed = int(new_speed)
                    print(f"The fan is now set to speed level {self.speed}.")
            else:
                print(f"The fan remains at speed level {self.speed}.")

    # Function to change fan direction setting (clockwise / counter-clockwise)
    def change_direction(self):
        if (self.status == "off"):
            print("The ceiling fan is currently turned off. It must be on to change the direction.")
            direction_choice = input("Do you wish to turn the fan on? (Y / N) ")

            while direction_choice.upper() not in ("Y", "N"):
                print("Please enter a valid selection.")
                direction_choice = input("Do you wish to turn the fan on? (Y / N) ")

            if (direction_choice.upper() == "Y"):
                self.status = "on"
                self.changeDirection()
            else:
                print("The fan will remain off.")

        else:
            old_direction = self.direction
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
                new_direction = input("Enter the new direction setting: (clockwise or counter-clockwise) ")

                while new_direction.lower() not in ("clockwise", "counter-clockwise"):
                    print("Please enter a valid selection.")
                    new_direction = input("Enter the new direction setting: (clockwise or counter-clockwise) ")

                self.direction = new_direction.lower()

                if (old_direction == self.direction):
                    print(f"The fan is already set to {self.direction} direction.")
                else:
                    print(f"The fan is now set to {self.direction} direction.")
            else:
                print(f"The fan will remain set to {self.direction} direction.")
