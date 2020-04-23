"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    Since we know the count down will start at 10, we can safely assign a constant to the number 10 and assign it as
    the range in our for loop to have it run 10 times.
    I also assigned a variable "countdown" to the value 10 so that at the end of each loop, countdown
    will be decremented by 1.
    After the for loop has completed running, I simply printed the string "Lift Off!"
    """
    COUNTDOWN_START = 10
    countdown = 10
    for i in range(COUNTDOWN_START):
        print(str(countdown) + '...')
        countdown -= 1
    print('Lift Off!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
