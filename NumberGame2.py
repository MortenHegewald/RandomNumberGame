import random

numOfGuesses = 0

number = random.randint(1,10)

print('Hi, what is your name?')
name = input()

print('Hi ' + name + '. I am thinking of a number between 1 and 10, try to guess it.')

while numOfGuesses < 5:
    print('Guess:')
    guess = int(input())

    numOfGuesses = numOfGuesses + 1
    if guess > number:
        print('Sorry, that was too high.')

    if guess < number:
        print('Sorry, that was too low.')

    if guess == number:
        break

if guess == number:
    numOfGuesses = str(numOfGuesses)
    print('Correct ' + name + '. You managed to guess the number in only ' + numOfGuesses + ' tries!')

if guess != number:
    number = str(number)
    print('The number I was thinking of was '+ number)