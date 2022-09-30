# put a number between two numbers
# tell computer to guess the number
# computer guess the number
# we check if the number is higher or lower than the given number
# if the number is higher than the given number, we set the number as the max value
# if the number is lower than the given number, we set the number as the min value

from random import randint

# MY IMPLEMENTATION 
# number_to_guess = int(input('Guess a number between 1 and 100: '))
# def computer_guess(number_to_guess):
#     min = 1
#     max = 1000
#     count = 0
#     guessed_by_computer = randint(min, max)

#     while number_to_guess != guessed_by_computer:
#         guessed_by_computer = randint(min, max)
#         count = count + 1
#         if guessed_by_computer > number_to_guess:
#             max = guessed_by_computer - 1
#         elif guessed_by_computer < number_to_guess:
#             min = guessed_by_computer + 1
#     return f"Made it after {count} guesses!"

# print(computer_guess(number_to_guess))

# Kylie Ying's IMPLEMENTATION 
def computer_guess2(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?');
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed the number, {guess} correctly!')

computer_guess2(10)