"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    print('Hailstones...')
    n = int(input('Please enter a positive integer: '))
    count = 0
    while n != 1:
        if n % 2 == 0:
            print(str(n) + ' is even, so half of it is: ' + str(n / 2))
            n = n / 2
            count += 1
        else:
            print(str(n) + ' is odd, so the value of 3n + 1 is: ' + str((n * 3) + 1))
            n = (n * 3) + 1
            count += 1
    print('Finished... The process took ' + str(count) + ' steps to reach 1.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
