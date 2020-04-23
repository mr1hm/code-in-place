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
    # check_surrounding()


def place_beepers_on_row():
    """
    Put beepers on the entire first row and remove outer-most beepers.
    This will effectively make a boundary on which Karel can move.
    """
    if front_is_blocked():  # A check for the smallest world (1x1).
        put_beeper()
    else:
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
    """
    When this function is called, it tells Karel to find the outer-most beepers and remove them.
    """
    if front_is_clear():  # A check to make sure that front_is_clear() (1x1).
        if beepers_present():
            pick_beeper()
            move()
            while beepers_present():  # Karel will move until he lands on the first corner with no beeper.
                move()  # In other words, Karel will move until it has reached the corner adjacent to the wall.
            reverse_direction()  # Face Karel in the opposite direction.
            while no_beepers_present():  # Karel will continue to move the opposite direction if there are no beepers.
                move()
                """
                We can safely assume that Karel will move until he arrives at a corner with a beeper (outer-most beeper).
                """
            pick_beeper()  # Then Karel will simply pick the outer-most beeper up.


def check_surrounding():
    """
    This function assumes Karel is now standing on a corner with no beeper.
    When this function is called, Karel checks to see if the front_is_clear() and if a beepers_present().
    If the front is not clear, Karel will simply turn to face the opposite direction.
    Else, Karel will check for a beeper. If a beeper exists, Karel will continue to move until Karel realizes
    it's a 8x8 world. In the case of an 8x8 world, the remove_outer_most_beepers() function is called to
    eliminate the remaining outer beepers.
    Finally, Karel will manually remove 1 of 2 remaining beepers in the 8x8 world and end up positioned on the
    remaining beeper.
    """
    while no_beepers_present():  # Karel will move until it reaches a corner with a beeper.
        if front_is_clear():  # For smaller world (2x2). If the front is clear keep moving.
            move()  # We can safely assume that this is the outer-most beeper.
        else:  # If the above condition isn't truthy, Karel will put a beeper down and stop.
            put_beeper()
    if beepers_present():
        """
        Since we know the largest world is 8x8, if a beeper is present,
        we will hard code a manual check for other beepers.
        ----
        The else statements will handle smaller worlds and the If statements
        will handle larger worlds.
        """
        if front_is_clear():  # This check is in place for smaller worlds (2x2 and under).
            # If the front_is_blocked(), the code will stop executing here. For smaller worlds.
            move()
            if beepers_present():  # If a beeper is present here, this means that there are 2 beepers.
                move()
                if beepers_present():  # If a beeper is present here, this means that there are 3 beepers.
                    move()
                    if beepers_present():  # If a beeper is present here, this means that there are 4 beepers.
                        move()
                        if beepers_present():  # If a beeper is present here, this means that there are 5 beepers.
                            move()
                            # If there is a larger world than 8x8, we can simply repeat remove_outer_most_beepers().
                            remove_outer_most_beepers()
                        else:
                            """
                            If the world size is 8x8, we can remove the remaining outer most beepers and find 
                            1 of the 2 beepers.
                            """
                            reverse_direction()
                            while no_beepers_present():
                                move()
                            remove_outer_most_beepers()
                            while no_beepers_present():
                                move()
                            if beepers_present():
                                move()
                                if beepers_present():
                                    move()
                                    if beepers_present():
                                        move()
                                    else:  # This code block handles removing 1 of 2 beepers remaining and landing on the beeper.
                                        reverse_direction()
                                        move()
                                        pick_beeper()
                                        move()
                    else:  # For 7x7 world.
                        reverse_direction()
                        while no_beepers_present():
                            move()
                        remove_outer_most_beepers()
                        while no_beepers_present():
                            move()
                else:
                    reverse_direction()
                    move()
            else:
                """
                If there is no 2nd beeper. Stop Karel, turn him around, and move back one corner to land on the midpoint.
                """
                reverse_direction()
                move()
        else:
            reverse_direction()


def reverse_direction():
    """
    Turns Karel around to face the opposite direction.
    """
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()