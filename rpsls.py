# Author: Arush Gupta
# Date: 2nd June, 2015
# Filename: rspls.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import math
import random

def name_to_number(name):

    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1

def number_to_name(number):

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "error"

def rpsls(player_choice): 
    player_number = name_to_number(player_choice)
    
    if player_number == -1:
        print "ERROR: Please choose rock, paper, scissors, lizard or Spock."
        return
    
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    
    print "Player chooses " + player_choice
    print "Computer chooses " + comp_choice
    result = (player_number - comp_number) % 5

    if result == 1 or result == 2:
        print "Player Wins!"
    elif result == 3 or result == 4:
        print "Computer Wins!"
    else:
        print "Player and Computer Tie!"
    print ""
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("name")

# always remember to check your completed program against the grading rubric
