#==============================================================================
# Filename: Karel_Painting.py
# 
# Your name: Kate Adams
# Who did you work with (if anyone)?: No
# If you consulted AI, which one? And link to transcript if available: No Ai
# Estimate for time spent on this prob (in hrs)?: 0.1 hr
#==============================================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit. Don't forget comments!

import karel

def main():
    """ Function to cause Karel to paint 3 sides of its house and then go indoors. """
    turn_left()
    turn_left()
    for i in range(3):
        paint_wall_reorient()
    move()
    turn_left()
    move()

def paint_wall():
    while left_is_blocked():
        put_beeper()
        move()
    
def paint_wall_reorient():
    paint_wall()
    turn_left()
    move()
