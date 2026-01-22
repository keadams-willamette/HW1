#===============================================================================
# Filename: Karel_Newspaper.py
# 
# Your name: Kate Adams
# Who did you work with (if anyone)?:No
# If you consulted AI, which one? And link to transcript if available:No Ai
# Estimate for time spent on this problem (in hrs)?: 0.2 hrs
#===============================================================================

# I've just laid out a basic starting function below. 
# While this problem is fairly simple, you should still practice
# the good habit of writing helper functions to decompose the problem
# into smaller pieces. I have provided you with a template for the
# main function and then 3 helping functions as outlined in the PDF

import karel


def main():
    """ Function to cause Karel to retrieve the newspaper. """
    move_to_newspaper()
    pick_beeper()
    return_to_start()


def move_to_newspaper():
    """ Helping function to move Karel to the newspaper location. """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def return_to_start():
    """ Helping function to move Karel back to its starting position. """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()