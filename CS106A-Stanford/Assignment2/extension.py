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
    if difficulty == 'e':
        print('This will test your addition and subtraction skills...')
    if difficulty == 'm':
        print('This will test your addition, subtraction and multiplication skills...')
    if difficulty == 'h':
        print('This will test your addition, subtraction, multiplication and division skills...')
    if difficulty == 'g':
        print('This will test your addition, subtraction, multiplication and division skills...')
    logic(difficulty)


def logic(difficulty):
    if difficulty == 'e':
        min_value = 0
        max_value = 50
        operators = ['+', '-']
    if difficulty == 'm':
        min_value = 0
        max_value = 75
        operators = ['+', '-', '*']
    if difficulty == 'h':
        min_value = 0
        max_value = 100
        operators = ['+', '-', '*', '/']
    if difficulty == 'g':
        min_value = 50
        max_value = 150
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
        print('What is ' + str(num1) + ' ' + operators[random_index] + ' ' + str(num2) + '?')
        user_answer = input('Your answer: ')
        if check_type(user_answer, answer, correct_answers):
            questions_remaining = 3 - correct_answers
            correct_answers += 1
            if correct_answers != 3:
                print('Correct! You have ' + str(questions_remaining - 1) +
                      ' questions remaining...')
            else:
                print('Correct!')
                if difficulty == 'e':
                    print('You mastered addition and subtraction!')
                if difficulty == 'm':
                    print('You mastered addition, subtraction and multiplication!')
                if difficulty == 'h':
                    print('Wow... Not bad...')
                if difficulty == 'g':
                    print('Okay okay... You are a math GOD')
        else:
            correct_answers = 0
            print("That's not quite right...")


def check_type(user_input, answer, correct_answers):
    user_input = int(user_input)
    if isinstance(user_input, int):
        if int(user_input) != answer:
            return False
        else:
            return True
    else:
        print("That's DEFINITELY not right...")
        return False


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
