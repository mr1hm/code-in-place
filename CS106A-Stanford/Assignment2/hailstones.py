"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    We simply print an introductory string to the console and run the hailstones_logic() function.
    """
    print('The Hailstone Sequence...')
    hailstones_logic()


def hailstones_logic():
    """
    First, we check to make sure that the integer the user has given is positive. If it's a negative integer,
    we run a while loop until the user enters a positive integer and reassign the variable 'n' to the valid integer.
    Since the logic of the hailstone sequence begins by checking whether or not the integer is even or odd, we use
    the modulus operator to check whether or not the integer when divided by 2 returns 0 or 1.
    If a 0 is returned, it means that there was no remainder and 2 was divided evenly among the integer.
    Else, we know that a remainder of greater than 0 was returned and can safely assume that the integer was a odd
    number.
    If the integer is even, we divide the integer by 2. Else (the integer was odd), we multiply the integer by 3 and
    add 1.
    A while loop is in place so that these 2 checks continuously run until our variable 'n' has reached the value of 1.
    """
    n = int(input('Please enter a positive integer: '))
    while n < 0:
        print("That's not a positive integer... ")
        n = int(input('Please enter a POSITIVE integer: '))
    count = 0
    while n != 1:
        if n % 2 == 0:
            print(str(n) + ' is even, so half of it is: ' + str(int(n / 2)))
            n = n / 2
            count += 1
        else:
            print(str(n) + ' is odd, so the value of 3n + 1 is: ' + str(int((n * 3) + 1)))
            n = (n * 3) + 1
            count += 1
    print('Finished... The process took ' + str(count) + ' steps to reach 1.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
