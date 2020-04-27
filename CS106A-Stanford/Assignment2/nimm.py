"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    start_game()
    game_logic()


def start_game():
    print('Welcome to the Ancient Game of Nimm...')
    print('Lets get started...')


def game_logic():
    """
    This function handles most of the game's logic. It will store player names into the variables
    'player1' and 'player2'.
    Then we set the starting amount of stones in the center pile to 20.
    The 'player1_move' variable reflects the fact that player1 will always move first.
    Most of the game's logic is nested in a while loop since we know that the game doesn't end until the
    'stones_remaining' has reached 0.
    The variable 'final_move' is initially assigned to 'player1', but we know that this is going to change anyway.
    We have a simple if else conditional to check for which players turn it is. If the if statement is deemed falsy,
    we know it's 'player2' turn and vice versa.
    Finally, when 'stones_remaining' reaches 0, we will exit the while loop and run a conditional check to see which
    player went last.
    I used a not operator to conclude whether 'player1_move' or 'player2_move' was falsy. If 'player1_move' is false,
    we know that 'player1' made the last move and vice versa.
    """
    player1 = input('Player 1, please enter your name: ')
    print('Player 1: ' + player1)
    player2 = input('Player 2, please enter your name: ')
    print('Player 2: ' + player2)
    stones_remaining = 20  # Game logic function
    player1_move = True
    player2_move = False
    while stones_remaining > 0:
        final_move = player1
        if player1_move:
            stones_to_remove = int(input(player1 + ', how many stones would you like to remove? '))
            if 0 < stones_to_remove < 3:
                print(player1 + ' removed ' + str(stones_to_remove) + ' stones.')
                stones_remaining -= stones_to_remove
                print('There are ' + str(stones_remaining) + ' stone(s) remaining...')
                player1_move = False
                player2_move = True
            else:
                print('There are ' + str(stones_remaining) + ' stone(s) remaining')
                print('Please specify a valid amount of stones to remove. Players can only remove 1 or 2 stones '
                      'per turn.')
        else:
            stones_to_remove = int(input(player2 + ', how many stones would you like to remove? '))
            if 0 < stones_to_remove < 3:
                print(player2 + ' removed ' + str(stones_to_remove) + ' stones.')
                stones_remaining -= stones_to_remove
                print('There are ' + str(stones_remaining) + ' stone(s) remaining...')
                player1_move = True
                player2_move = False
            else:
                print('There are ' + str(stones_remaining) + ' stone(s) remaining')
                print('Please specify a valid amount of stones to remove. Players can only remove 1 or 2 stones '
                      'per turn.')
    if stones_remaining == 0:
        if not player1_move:
            final_move = player1
            print(player2 + ' wins!')
        if not player2_move:
            final_move = player2
            print(player1 + ' wins!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
