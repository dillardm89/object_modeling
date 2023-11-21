from ..user.usernewfaninput import (change_num_blades, change_num_bulbs)
from fanprintstatus import get_fan_status_statement


# Create a class to model a Ceiling Fan object
class CeilingFan:
    def __init__(self, name, id=None, fan_status="off",
                 light_status="off", blades=None, bulbs=None,
                 speed=0, light_setting=0, direction="counter-clockwise"):

        self.name = name
        self.id = id
        self.fan_status = fan_status.lower()
        self.light_status = light_status.lower()
        self.blades = blades
        self.bulbs = bulbs
        self.speed = speed
        self.light_setting = light_setting
        self.direction = direction.lower()
        self.set_blades()
        self.set_bulbs()

    # Return string when print(class object) called
    def __str__(self):
        statement = get_fan_status_statement(self)
        print(statement)
        return ""

    # Function to return fan details
    def get_fan_details(self):
        details = (self.fan_status, self.light_status, self.speed,
                   self.light_setting, self.direction, self.name)
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
    def change_fan_status(self, fan_status):
        self.fan_status = fan_status

    # Function to change light status (on/off)
    def change_light_status(self, light_status):
        self.light_status = light_status

    # Function to change fan speed setting (1-3)
    def change_speed(self, speed):
        self.speed = speed

    # Function to change fan light setting (1-5)
    def change_light_setting(self, light_setting):
        self.light_setting = light_setting

    # Function to change fan direction setting (clockwise / counter-clockwise)
    def change_direction(self, direction):
        self.direction = direction
