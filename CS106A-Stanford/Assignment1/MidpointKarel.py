from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    place_beepers_on_row()
    remove_outer_most_beepers()
    check_surrounding()


def place_beepers_on_row():
    """
    Put beepers on the entire first row and remove outer-most beepers.
    This will effectively make a boundary on which Karel can move.
    """
    while front_is_clear():  # keep putting beepers on all corners until front_is_blocked().
        put_beeper()
        move()
    reverse_direction()  # when Karel stops, we know he's reached the wall, so we can simply reverse his direction.
    while front_is_clear():  # same idea here.
        move()
    if beepers_present():  # while also the same idea, Karel will pick up the beeper that's on the first corner of the wall.
        pick_beeper()
    reverse_direction()
    move()


def remove_outer_most_beepers():
    if beepers_present():
        pick_beeper()
        move()
        while beepers_present():  # Karel will move until he lands on the first corner with no beeper.
            move()  # In other words, Karel will move until it has reached the corner adjacent to the wall.
        reverse_direction()  # Face Karel in the opposite direction.
        while no_beepers_present():  # Karel will continue to move the opposite direction if there are no beepers.
            move()  # We can safely assume that Karel will move until he arrives at a corner with a beeper (outer-most beeper).
        pick_beeper()  # Then Karel will simply pick the outer-most beeper up.


def check_surrounding():  # This function assumes Karel is now standing on a corner with no beeper.
    while no_beepers_present():  # Karel will move until it reaches a corner with a beeper.
        move()  # We can safely assume that this is the outer-most beeper.
    if beepers_present():  # If a beeper is present, we will hard code a manual check for other beepers.
        move()
        if beepers_present():  # If a beeper is present here, this means that there are 2 beepers.
            move()
        else:  # If there is no 2nd beeper. Stop Karel, turn him around, and move back one corner to land on the midpoint.
            reverse_direction()
            move()
    else:
        reverse_direction()


# def check_surrounding_corners():
#     if corner_color_is(PINK):
#         move()
#     if corner_color_is(ORANGE):
#         reverse_direction()
#         move()
#         move()
#         if corner_color_is(ORANGE):
#             reverse_direction()
#             move()
#         else:
#             move()


# def move_while_paint_is_gray():
#     while corner_color_is(GRAY):
#         move()


def reverse_direction():
    turn_left()
    turn_left()


def return_to_beeper_position():
    turn_left()
    turn_left()
    while no_beepers_present():
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()