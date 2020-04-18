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
    # reverse_direction()
    # eliminate_gray_corners()
    # check_surrounding_corners()
    # turn_left_and_move()
    # eliminate_gray_corners()


def place_beepers_on_row():
    while front_is_clear():  # keep putting beepers on all corners until front_is_blocked().
        put_beeper()
        move()
    reverse_direction()  # when Karel stops, we know he's reached the wall, so we can simply reverse his direction.
    while front_is_clear():  # same idea here.
        move()
    if beepers_present():  # while also the same idea, Karel will pick up the beeper that's on the first corner of the wall.
        pick_beeper()
    reverse_direction()
    while no_beepers_present():  # at this point, Karel should have removed the outer-most beepers and we'll have him move until there are beepers present.
        move()
    if beepers_present():
        move()
        if beepers_present():
            move()
            if beepers_present():
                pick_beeper()



def eliminate_gray_corners():
    if corner_color_is(BLUE):  # if corner color is blue, move to next corner.
        move()
    while corner_color_is(GRAY):  # paint outer gray corners orange, effectively making orange the new boundary.
        paint_corner(ORANGE)
        move()
    if corner_color_is(BLUE):
        reverse_direction()
        move()
    if corner_color_is(ORANGE):
        move()
        paint_corner(PINK)
        move()
    while front_is_clear():
        move()
    reverse_direction()
    while corner_color_is(BLUE) or corner_color_is(ORANGE):
        move()


def check_surrounding_corners():
    if corner_color_is(PINK):
        move()
    if corner_color_is(ORANGE):
        reverse_direction()
        move()
        move()
        if corner_color_is(ORANGE):
            reverse_direction()
            move()
        else:
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
