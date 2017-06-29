# My stab at the guessTheNumber program from Chapter 3

import random

print('I\'m thinking of a number between 1 and 20')

r = random.randint(1,20)
guess = 0
guesses = 0

while int(guess) != r:
    print('Take a guess. Hint: ' + str(r))
    guess = input()
    guesses += 1
    try:
        if int(guess) > r:
            print('Your guess is too high.')
        elif int(guess) < r:
            print('Your guess is too low.')
    except:
        print('Guess must be a number you idiot!')

print('Good job! You guessed the number in ' + str(guesses) + ' guesses!')
