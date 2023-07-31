import random

#first iteration

"""
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print('The estimation is too low, go higher')
        if guess > random_number:
            print('The estimation is too high, go lower')
        if guess == random_number:
            print('You guessed the correct answer!')   
    print(guess)
    
guess(20)

"""

#Second iteration, adding the ability to add a custom limit
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print('The estimation is too low, go higher')
        if guess > random_number:
            print('The estimation is too high, go lower')
        if guess == random_number:
            print('You guessed the correct answer!')   
    print(guess)
    
print('Before we begin the guessing game, you must pick a number, which will limit the range \
      for example, if you choose 15, you will guess a number between 1 and 15')
num = int(input('Please choose a number:'))
guess(num)