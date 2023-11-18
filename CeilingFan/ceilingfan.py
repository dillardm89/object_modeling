from userinput import validate_type_is_int
from userinput import validate_type_is_str
from userinput import change_status_input
from userinput import change_speed_input
from userinput import change_direction_input
from usermessages import return_success_msg


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
        if self.status == "off":
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
            numBlades = 0
            valid_input_type = False
            while (valid_input_type is not True and
                   numBlades not in ("3", "4", "5", "6")):
                numBlades = input("How many blades does your " +
                                  "ceiling fan have? (3-6) ")

            self.blades = int(numBlades)
        else:
            return

    # Function to set number of light bulbs
    def set_bulbs(self):
        if self.bulbs is None:
            numBulbs = 0
            valid_input_type = False
            while (valid_input_type is not True and
                   numBulbs not in ("1", "2", "3", "4", "5")):
                numBulbs = input("How many light bulbs does your " +
                                 "ceiling fan have? (1-5) ")

            self.bulbs = int(numBulbs)
        else:
            return

    # Function to change fan status (on/off)
    def change_status(self):
        old_status = self.status
        print(f"The fan is currently turned {self.status}.")

        if old_status == "off":
            proposed_staus = "on"
        else:
            proposed_staus = "off"

        choice = ""
        valid_input_type = False
        while (valid_input_type is not True and
               choice.upper() not in ("Y", "N")):
            choice = input("Do you wish to turn the fan " +
                           f"{proposed_staus}? (Y / N) ")
            valid_input_type = validate_type_is_str(choice)

        if (choice.upper() == "Y"):
            self.status = proposed_staus
            action_type = f"turned {proposed_staus}"
            return_success_msg(self.user_name, action_type)
        else:
            print(f"Fan named {self.user_name} remained turned {self.status}.")

    # Function to change fan speed setting (1-3)
    def change_speed(self):
        if (self.status == "off"):
            change_type = "speed"
            status = change_status_input(self.status, self.user_name,
                                         change_type)

            if status == "off":
                return

        old_speed = self.speed
        print(f"The fan is currently at speed level {self.speed}.")
        choice = change_speed_input()

        if (choice.upper() == "Y"):
            new_speed = 0
            speed_input_type = False
            while (speed_input_type is not True and
                   int(new_speed) < 1 or int(new_speed) > 3):
                new_speed = input("Enter the new speed setting from 1-3: ")
                speed_input_type = validate_type_is_int(new_speed)

            if (old_speed == new_speed):
                print("The fan is already set to speed " +
                      f"level {self.speed}.")
            else:
                self.speed = int(new_speed)
                action_type = f"changed to speed level {self.speed}"
                return_success_msg(self.user_name, action_type)
        else:
            print(f"The fan named {self.user_name} remains " +
                  "at speed level {self.speed}.")

    # Function to change fan direction setting (clockwise / counter-clockwise)
    def change_direction(self):
        if (self.status == "off"):
            change_type = "direction"
            status = change_status_input(self.status, self.user_name,
                                         change_type)

            if status == "off":
                return

        old_direction = self.direction
        print("The ceiling fan is currently set " +
              f"to {self.direction} direction.")

        if (self.direction == "clockwise"):
            print("This is the ideal winter direction setting.")
        else:
            print("This is the ideal summer direction setting.")

        choice = change_direction_input()
        if (choice.upper() == "Y"):
            new_direction = ""
            valid_input_type = False
            while (valid_input_type is not True and new_direction.lower()
                   not in ("clockwise", "counter-clockwise")):
                new_direction = input("Enter the new direction setting: " +
                                      "(clockwise or counter-clockwise) ")
                valid_input_type = validate_type_is_str(new_direction)

            if (old_direction == self.direction):
                print("The fan is already set to " +
                      f"{self.direction} direction.")
            else:
                self.direction = new_direction.lower()
                action_type = f"changed to direction setting: {self.direction}"
                return_success_msg(self.user_name, action_type)
        else:
            print(f"The fan named {self.user_name} remains " +
                  "at direction setting: {self.direction}.")
