#   
#   Filename: robot.py
#
#   ROBOT FIGHT CLUB 2 - PYTHON EDITION
#   A class holding the template for the robot objects
#
#   Name:   Matt Delaney
#   Date:   December 11th, 2021
#
#
class robot:
    
    name        = ""        # The name of this robot
    
    health      = 25        # The starting health of the robot
    isAlive     = True      # If the robot is alive


    # Constructor, names the robot
    def __init__(self, name):
        self.name = name

    # Removes health from the robot object
    def take_damage(self, damage):
        self.health -= damage

    
