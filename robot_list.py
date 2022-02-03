#   
#   Filename: robot_fight_club.py
#
#   ROBOT FIGHT CLUB 2 - PYTHON EDITION
#   A template for robot lists
#
#   Name:   Matt Delaney
#   Date:   December 11th, 2021
#
#

# Import statements
from os import close        # Close Files
import robot as r           # Robot Class
from Lib import random      # Random Numbers

class list_of_robots:

    number_of_robots = 0            # The number of requested robots
    name_list = []                  # The entire list of possible robot names

    active_robot_list = []          # List of all the active robots
    
    
    def open_name_file(self):
        # Opens a predefined text file

        path = "robot_names.txt"    # The path to the file
        mode = "r"                  # The mode of the open function (r = read)
        
        #TODO: Use 'with?' and also use a try catch block
        name_file = open(path, mode)            # Opens file
        self.name_list = name_file.readlines()  # Puts lines into a list
        name_file.close()                       # Closes file


    @staticmethod
    def get_next_random_robot(self) -> str:
        # Returns the next random name from names_list

        local_names_list = []
        
        if len(local_names_list) == 0:
            local_names_list.extend(self.name_list)
            random.shuffle(local_names_list)

        popped_name = local_names_list.pop().rstrip()

        return popped_name



    def add_robots(self):
        #TODO: Add number_of_robots as a local variable, remove from class
        #TODO: Replace strings with robot objects

        local_names_list = []
        local_names_list.extend(self.name_list)
        random.shuffle(local_names_list)
        
        if self.number_of_robots <= len(self.name_list):
            self.active_robot_list.append(self.get_next_random_robot(self))
        
        elif self.number_of_robots > len(self.name_list):
            
            loop_rounds = 0
            names_added = 0

            while names_added < self.number_of_robots:

                if (names_added % len(self.name_list)) == 0:
                    loop_rounds = loop_rounds + 1

                append_str = f"_{loop_rounds}"

                name = self.get_next_random_robot(self)
                name += append_str
                self.active_robot_list.append(name)

                names_added = names_added + 1

            
            
    
    
    def __init__(self, number_of_robots):
        # Initializes the robot list with a defined number of robots
        
        # Sets the number of requested robots to parameter of the function
        self.number_of_robots = number_of_robots

        # Populates list_of_names
        self.open_name_file()

        self.add_robots()

                  

    