"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_VALUE = 0
MAX_VALUE = 100


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    guess_correct_sum()


def guess_correct_sum():
    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(MIN_VALUE, MAX_VALUE)
        num2 = random.randint(MIN_VALUE, MAX_VALUE)
        sum_numbers = num1 + num2
        print('What is ' + str(num1) + ' + ' + str(num2) + '?')
        user_answer = int(input('Your Answer: '))
        if user_answer == sum_numbers:
            correct_answers += 1
            print('Correct Answers: ' + str(correct_answers))
        else:
            correct_answers = 0
            print("That's not quite right...")
            print('The answer was: ' + str(sum_numbers))
    print("Congratulations, you are now a Math genius!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
