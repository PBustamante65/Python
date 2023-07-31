import random

def play():
    user = input('Pick one: (r) rock, (p) paper, (s) scissors\n' )
    computer = random.choice(['r','p','s'])
    print(f'The computer chose {computer}')


    if user == computer:
        return 'Tie'
    
    if player_win(user, computer):
        return 'You win'
    
    return 'You lost'

def player_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

print(play())