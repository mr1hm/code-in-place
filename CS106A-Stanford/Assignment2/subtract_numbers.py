"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    Since Part 1-A asks us to use real numbers (float), assuming the user always inputs
    a decimal point number we can wrap input() in float(). That way, when a decimal
    point number is entered, Python can correctly convert the string to a real number.
    Once the strings have been converted to real numbers, we can use the mathematical expression
    (num1 - num2) to have Python calculate the difference between the two real numbers.
    """
    print('Subtract Two Real Numbers...')
    num1 = float(input('Enter First Number: '))
    num2 = float(input('Enter Second Number: '))
    difference = num1 - num2
    print('The difference is: ' + str(difference))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
