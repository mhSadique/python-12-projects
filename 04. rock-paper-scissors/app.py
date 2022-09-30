import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return 'You won'
    return 'You lost'

def is_win(user, computer):
# logic : r > s, p > r, s > p 
    if  (user == 'r' and computer == 's') or \
        (user == 'p' and computer == 'r') or \
        (user == 's' and computer == 'p'):
        return True

print(play())