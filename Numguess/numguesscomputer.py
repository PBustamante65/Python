import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too low? (L), too high? (H), or correct? (C)').lower()
        if feedback == 'h':
            high = high-1
        elif feedback == 'l':
            low = low + 1
    print(f'I won, the number was {guess}')

computer_guess(10)