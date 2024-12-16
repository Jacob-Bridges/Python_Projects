# Jacob Bridges
# 2/2/2024
# This program will roll a 20 sided die and display the roll and symbol

import random


# main module
def main():
    # Get the number of rolls. Number has to be between 5 and 15
    rolls = int(input('How many times do you want to roll the die? '))
    # Input validation:
    # while number of rolls is less than 5 or rolls is more than 15, print disclaimer and ask user for new input
    while rolls < 5 or rolls > 15:
        print('Enter a number between 5 and 15.')
        rolls = int(input('How many times do you want to roll the die? '))
    # Pass input argument for number of rolls to roll_die function
    roll_die(rolls)


# roll_die pulls the value for the number of times the user wants to roll the die
def roll_die(total_rolls):
    for i in range(1, total_rolls + 1):
        dice_roll = random.randint(1, 20)
        if dice_roll == 20:
            symbol = 'CRITICAL HIT!'
        elif dice_roll % 4 == 0:
            symbol = 'Sword'
        elif dice_roll % 4 == 1:
            symbol = 'Shield'
        elif dice_roll % 4 == 2:
            symbol = 'Spell'
        elif dice_roll % 4 == 3:
            symbol = 'Potion'
        print(f'Roll {i}: {dice_roll} ==> {symbol}')
    print('Thanks for playing!')


# Call the main function
main()
