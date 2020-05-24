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
    We simply call the guess_correct_sum() function.
    """
    guess_correct_sum()


def guess_correct_sum():
    """
    Since the user has to guess 3 addition problems correctly in order to win, I first create a variable that tracks
    the amount of correct_answers.
    I then create a while loop to continuously run until correct_answers has reached a value of 3.
    I used the random library to have Python generate random numbers based on the constant MIN_VALUE and MAX_VALUE.
    The sum_numbers variable stores the correct answer.
    Then it asks the user for an input which is stored in user_answer.
    If the user_answer is equal to sum_numbers, then correct_answers is incremented by 1.
    Else, correct_answers is reset to 0 and we print the correct answer to the terminal.
    """
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
