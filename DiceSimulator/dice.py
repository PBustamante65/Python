import random
import os

"""
#first iteration, simple 2 dice simulator
def num_dice():
    while True:
        try:
            num_die = input("Number of dice to roll:")
            valid_inputs = ['1','2','one','two']
            if  num_die not in valid_inputs:
                raise ValueError('Please select either 1 or 2')
            return num_die
        except ValueError as Err:
            print(Err)

def roll_dice():
    min_lim = 1
    max_lim = 6
    roll_again = 'y'

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_dice()

        if amount == '2' or amount == 'two':
            print('Rolling the dice')
            dice1 = random.randint(min_lim,max_lim)
            dice2 = random.randint(min_lim,max_lim)

            print(f'Dice one: {dice1}')
            print(f'Dice two: {dice2}')
            print('total:', dice1 + dice2)

            roll_again = input('Roll again?')

        else:
            print('Rolling die: ')
            dice1 = random.randint(min_lim,max_lim)

            print(f'Dice one: {dice1}')

            roll_again = input('Roll again?')

roll_dice()

"""

#for the second iteration, we add 2 more dice, of 20 sides each
def num_dice():
    while True:
        try:
            num_die = input("Number of dice to roll:")
            valid_inputs = ['1','2','3','4','one','two','three','four']
            if  num_die not in valid_inputs:
                raise ValueError('Please select between 1 or 4 dice to roll:')
            return num_die
        except ValueError as Err:
            print(Err)

def roll_dice():
    min_lim = 1
    max_lim = 20
    roll_again = 'y'

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_dice()

        if amount == '4' or amount == 'four':
            print('Rolling the dice...')
            dice1 = random.randint(min_lim,max_lim)
            dice2 = random.randint(min_lim,max_lim)
            dice3 = random.randint(min_lim,max_lim)
            dice4 = random.randint(min_lim,max_lim)

            print(f'\nDice one: {dice1}')
            print(f'Dice two: {dice2}')
            print(f'Dice three: {dice3}')
            print(f'Dice four: {dice4}')
            print('\nTotal:', dice1 + dice2 + dice3 + dice4)

            roll_again = input('Roll again?')

        elif amount == '3' or amount == 'three':
            print('Rolling the dice...')
            dice1 = random.randint(min_lim,max_lim)
            dice2 = random.randint(min_lim,max_lim)
            dice3 = random.randint(min_lim,max_lim)

            print(f'\nDice one: {dice1}')
            print(f'Dice two: {dice2}')
            print(f'Dice three: {dice3}')
            print('\nTotal:', dice1 + dice2 + dice3)

            roll_again = input('Roll again?')


        elif amount == '2' or amount == 'two':
            print('Rolling the dice')
            dice1 = random.randint(min_lim,max_lim)
            dice2 = random.randint(min_lim,max_lim)

            print(f'\nDice one: {dice1}')
            print(f'Dice two: {dice2}')
            print('Total:', dice1 + dice2)

            roll_again = input('Roll again?')

        elif amount == '1' or amount == 'one':
            print('Rolling die: ')
            dice1 = random.randint(min_lim,max_lim)

            print(f'\nDice one: {dice1}')

            roll_again = input('Roll again?')

roll_dice()