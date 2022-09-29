import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} :"))
        if guess < random_number:
            print('To low. Try again.')
        elif guess > random_number:
            print('To high. Try again.')
        else:
            print('YAY! You did it! Congrats!')

print(guess(5))