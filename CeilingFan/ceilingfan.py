from userfunctions import change_num_blades
from userfunctions import change_num_bulbs


# Create a class to model a Ceiling Fan object
class CeilingFan:
    def __init__(
        self, name, id=None, status="off", blades=None,
            bulbs=None, speed=1, direction="counter-clockwise"):

        self.name = name
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
            return f"{self.id}: Fan named '{self.name}' is turned " +\
                f"{self.status}. It is equipped with {self.blades} blades " +\
                f"and {self.bulbs} light bulbs."
        else:
            return f"{self.id}: Fan named '{self.name}' is turned " +\
                f"{self.status}. It is equipped with {self.blades} blades " +\
                f"and {self.bulbs} light bulbs. It is currently moving in " +\
                f"{self.direction} direction at speed level {self.speed}."

    # Function to return fan details
    def get_fan_details(self):
        details = (self.status, self.speed, self.direction, self.name)
        return details

    # Function to set number of fan blades
    def set_blades(self):
        if self.blades is None:
            self.blades = change_num_blades()
        else:
            return

    # Function to set number of light bulbs
    def set_bulbs(self):
        if self.bulbs is None:
            self.bulbs = change_num_bulbs()
        else:
            return

    # Function to change fan status (on/off)
    def change_status(self, status):
        self.status = status

    # Function to change fan speed setting (1-3)
    def change_speed(self, speed):
        self.speed = speed

    # Function to change fan direction setting (clockwise / counter-clockwise)
    def change_direction(self, direction):
        self.direction = direction
