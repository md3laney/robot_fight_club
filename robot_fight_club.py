#   
#   Filename: robot_fight_club.py
#
#   ROBOT FIGHT CLUB 2 - PYTHON EDITION
#   The main file for Robot Fight Club, imports other helper classes
#   Name:   Matt Delaney
#   Date:   December 11th, 2021
#
#

# Import Statements
import robot as r
from robot_list import list_of_robots

x = list_of_robots(30)

for index in x.active_robot_list:
    print(index)