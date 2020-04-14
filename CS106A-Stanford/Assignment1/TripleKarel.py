from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    Since there will always be 3 buildings, we can safely assume that Karel will have to
    perform the same operations 3 times.
    Since we also know that Karel will always start facing West and adjacent to a building wall
    the move_to_end_of_building_wall() function will repeat twice with a for loop to paint
    the first two walls of a given building. Since a for loop will repeat all of the code written inside its
    code block, and we don't want Karel to turn left after it has completed painting the third wall, the for
    loop is only repeated twice and the function move_to_end_of_building_wall() is called again separately
    after the for loop has finished executing.
    A conditional if statement is used to test if Karel is now facing a building wall.
    If it's true, Karel will turn right and repeat the same operation to paint three sides of the building.
    """
    for i in range(2):
        move_to_end_of_building_wall()
        turn_left()
        move()
    move_to_end_of_building_wall()
    if front_is_blocked():
        turn_right()
        for x in range(2):
            move_to_end_of_building_wall()
            turn_left()
            move()
    move_to_end_of_building_wall()
    if front_is_blocked():
        turn_right()
        for y in range(2):
            move_to_end_of_building_wall()
            turn_left()
            move()
    move_to_end_of_building_wall()


def move_to_end_of_building_wall():
    """
    Tests to see if there are no beepers present in the block.
    If there aren't any beepers present, a while loop is used to test if Karel's
    left side is blocked by a wall. As long as this condition holds true, Karel will
    place a beeper and move.
    """
    if no_beepers_present():
        while left_is_blocked():
            put_beeper()
            move()


def turn_right():
    """
    Turns Karel right by turning left three times.
    """
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
