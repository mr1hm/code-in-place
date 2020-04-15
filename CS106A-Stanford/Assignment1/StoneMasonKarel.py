from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    fix_pillars() is repeated four times in a for loop. Four represents the number of pillars given in each world.
    """
    for x in range(4):
        fix_pillars()


def fix_pillars():
    """
    Since we know for a fact that Karel's starting positioning will always be on the first row
    and first column facing East, we can safely assume that Karel's position is on the first supporting
    pillar.
    I turn Karel left to face North and use a while statement so that as long as the front_is_clear(), Karel
    will continue to check if there are no beepers present, place a beeper if it isn't, and move one block.
    As soon as front_is_clear() no longer holds true (we can assume that we have reached the top of the pillar),
    Karel will check to see if there are no beepers present on the current block and place one if there isn't.
    Karel will then turn_left() twice to face South and then repeat the first process of climbing up a pillar
    except in the opposite direction as long as the front_is_clear().
    When Karel reaches the bottom of a pillar, it will turn_left() and check to see if the
    front_is_clear(). If the front_is_clear(), Karel will proceed to move four times to the East.
    This process will repeat for a total of four times. Four represents the number of pillars that are
    present in any given world for this assignment.
    """
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        for y in range(4):
            move()


def turn_right():
    """
    Turns Karel right by turning left three times.
    """
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
