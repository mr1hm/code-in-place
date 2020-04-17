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
    paint_first_row()
    reverse_direction()
    eliminate_gray_corners()
    # turn_left_and_move()
    # eliminate_gray_corners()


def paint_first_row():
    paint_corner(BLUE)
    while front_is_clear():
        move()
        if corner_color_is(BLANK):
            paint_corner(GRAY)
    paint_corner(BLUE)


def eliminate_gray_corners():
    if corner_color_is(BLUE):
        move()
        if corner_color_is(GRAY):
            paint_corner(BLUE)
            move()
            while corner_color_is(GRAY):
                move()


def move_while_paint_is_gray():
    while corner_color_is(GRAY):
        move()


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
