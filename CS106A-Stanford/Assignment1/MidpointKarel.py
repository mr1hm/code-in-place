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
    # eliminate_gray_corners()
    # check_surrounding_corners()
    # turn_left_and_move()
    # eliminate_gray_corners()


def place_beepers_on_row():
    """
    Put beepers on the entire first row and remove outer-most beepers.
    This will effectively make a boundary on which Karel can move.
    """
    while front_is_clear():  # keep putting beepers on all corners until front_is_blocked().
        put_beeper()
        move()
    reverse_direction()  # when Karel stops, we know he's reached the wall, so we can simply reverse his direction.
    while front_is_clear():  # same idea as above here except in the opposite direction.
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
            move()
            if front_is_blocked():  # Do we need this?
                reverse_direction()
        while no_beepers_present():  # Karel will continue to move as long as there are no beepers.
            move()  # We can safely assume that Karel will move until he is standing on a corner with a beeper.
        pick_beeper()


def check_surrounding():




# def reverse_direction():
#     turn_left()
#     turn_left()
#
#
# def return_to_beeper_position():
#     turn_left()
#     turn_left()
#     while no_beepers_present():
#         move()


# There is no need to edit code beyond this point

    if __name__ == "__main__":
        run_karel_program()
