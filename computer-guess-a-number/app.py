# put a number between two numbers
# tell computer to guess the number
# computer guess the number
# we check if the number is higher or lower than the given number
# if the number is higher than the given number, we set the number as the max value
# if the number is lower than the given number, we set the number as the min value

from random import randint

number_to_guess = int(input('Guess a number between 1 and 100: '))

def computer_guess(number_to_guess):
    min = 1
    max = 1000
    count = 0
    guessed_by_computer = randint(min, max)

    while number_to_guess != guessed_by_computer:
        guessed_by_computer = randint(min, max)
        count = count + 1
        if guessed_by_computer > number_to_guess:
            max = guessed_by_computer - 1
        elif guessed_by_computer < number_to_guess:
            min = guessed_by_computer + 1
    return f"Made it after {count} guesses!"

print(computer_guess(number_to_guess))
