
import random


def main():
    """
    First, I initialize user_selection_incorrect to TRUE so that it triggers the while loop to run as long as
    user_selection_incorrect is TRUE.
    In the while loop, the terminal asks the user for a response of 'fate' or 'specify', if the user response is neither
    of these, the while loop will continue to run until the user responds with one of the 2 values. If the user responds
    with one of the 2 values, I reassign the user_selection_incorrect variable to FALSE and the while loop will no
    longer run.
    The if conditions that follow afterwards are to check which of the 2 values was specified. If it was 'fate', the
    program will call the random_tip() function to generate a random tip float value and then run calculations for
    the check total + tip. If it was 'specify', the program will ask the user to input a tip amount and then call the
    calculate_grand_total() function.
    """
    print('Tip Calculator v1.0...')
    user_selection_incorrect = True
    check_amount = float(input('Please enter the check total: '))
    print("If you would like to specify a tip amount (in percentage) please type 'specify' and press enter. "
          "Otherwise, you can let fate decide by typing 'fate' and pressing enter")
    while user_selection_incorrect:
        user_selection = input("Please enter your response (either 'specify' or 'fate'): ")
        if user_selection == 'specify' or user_selection == 'fate':
            user_selection_incorrect = False
    if user_selection == 'fate' or user_selection == 'specify':
        if user_selection == 'fate':
            fate_tip_total = random_tip(check_amount)
            fate_grand_total = calculate_grand_total(check_amount, fate_tip_total)
            print('Original Check Amount:', '$' + str(check_amount))
            print('Tip Total:', '$' + str(fate_tip_total))
            print('Grand Total:', '$' + str(fate_grand_total))
        else:
            tip_amount = input("Please enter the amount you want to tip in percent (i.e. '20%'): ")
            tip_float = percentage_to_float(tip_amount)
            tip_total = calculate_tip(check_amount, tip_float)
            grand_total = calculate_grand_total(check_amount, tip_total)
            print('Original Check Amount:', '$' + str(check_amount))
            print('Tip Total:', '$' + str(tip_total))
            print('Grand Total:', '$' + str(grand_total))
    else:
        print('Please enter a proper value...')
        while user_selection != 'fate' or user_selection != 'specify':
            user_selection = input("Please enter either 'specify' or 'fate': ")


def percentage_to_float(percentage):
    return float(percentage.strip('%')) / 100


def calculate_tip(check_amount, tip):
    tip_total = check_amount * tip
    return round(tip_total, 2)


def calculate_grand_total(check_amount, tip_total):
    grand_total = check_amount + tip_total
    return round(grand_total, 2)


def random_tip(check_amount):
    random_float = round(random.uniform(0, 1), 2)
    percentage = "{:.0%}".format(random_float)
    print('Random Tip:', percentage)
    return calculate_tip(check_amount, random_float)


if __name__ == '__main__':
    main()
