#!/usr/bin/python

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if  number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if  name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4

def rpsls(name): 
    # fill in your code below
    print 'Player chooses', name
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4, 1)
     # convert comp_number to name using number_to_name
    print 'Computor chooses', number_to_name(comp_number)
    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5
    # use if/elif/else to determine winner  
    #  result is 3 ,4 lose, is 1, 2 win, is 0 tie
    #  print results
    if  (result == 1) or (result == 2):
        print 'Player wins'
    elif (result == 3) or (result == 4):
        print 'Computor wins'
    else:
        print 'Player and Computor tie'
    
    print '=========================='
# test your code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric


