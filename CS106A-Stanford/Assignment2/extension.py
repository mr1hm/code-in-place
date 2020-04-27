"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""

from random import randint
from threading import Timer


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    difficulty = input("Please select a difficulty ('e' for easy, 'm' for medium, 'h' for hard, 'g' for genius): ")
    logic(difficulty)
    if difficulty == 'e':
        print('This will test your addition and subtraction skills...')
        print('You have 10 seconds to guess a correct answer for each problem...')
    if difficulty == 'm':
        print('This will test your addition, subtraction and multiplication skills...')
        print('You have 10 seconds to guess a correct answer for each problem...')
    if difficulty == 'h':
        print('This will test your addition, subtraction, multiplication and division skills...')
        print('You have 10 seconds to guess a correct answer for each problem...')
    if difficulty == 'g':
        print('This will test your addition, subtraction, multiplication and division skills...')
        print('You have 5 seconds to guess a correct answer for each problem...')


def logic(difficulty):
    if difficulty == 'e':
        min_value = 0
        max_value = 50
        time_given = 10
        operators = ['+', '-']
    if difficulty == 'm':
        min_value = 0
        max_value = 75
        time_given = 10
        operators = ['+', '-', '*']
    if difficulty == 'h':
        min_value = 0
        max_value = 100
        time_given = 10
        operators = ['+', '-', '*', '/']
    if difficulty == 'g':
        min_value = 50
        max_value = 150
        time_given = 5
        operators = ['+', '-', '*', '/']
    correct_answers = 0
    while correct_answers < 3:
        num1 = randint(min_value, max_value)
        num2 = randint(min_value, max_value)
        random_index = randint(0, (len(operators) - 1))
        if operators[random_index] == '+':
            answer = num1 + num2
        if operators[random_index] == '-':
            answer = num1 - num2
        if operators[random_index] == '*':
            answer = num1 * num2
        if operators[random_index] == '/':
            answer = num1 / num2
        print('What is ' + str(num1) + operators[random_index] + str(num2) + '?')
        print('Timer has started...')
        Timer(time_given, countdown_and_check_input).start()
        user_answer = int(input('Your answer: '))
        if user_answer == '':
            print('Make sure to enter a integer value...')
            return


def countdown_and_check_input():
    print('Sorry, you missed your chance!')
    return


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
