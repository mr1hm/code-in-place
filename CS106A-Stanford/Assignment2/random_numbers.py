"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random


def main():
    """
    Part 1-B asks us to write a program that will generate and print 10 random integers to the terminal.
    Constants are assigned for the amount of times Python will generate a random number, the minimum random integer,
    and maximum random integer. Additionally, I added a num_label variable so that each random integer generated is
    labeled in an orderly fashion.
    A for loop is used to run the random.randint() function 10 times automatically and increments num_label
    by 1 every time a single loop has completed.
    """
    NUM_RANDOM = 10
    MIN_RANDOM = 0
    MAX_RANDOM = 100
    num_label = 1
    print('Printing ten random integers...')
    for i in range(NUM_RANDOM):
        print(str(num_label) + '):' + ' ' + str(random.randint(MIN_RANDOM, MAX_RANDOM)))
        num_label += 1


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
