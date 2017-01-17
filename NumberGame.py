import random

number = random.randint(1,10)

response = int(input("Try to guess the nunber :-) "))

if response < number:
    print('Sorry, too low. The number was ' + str(number))
elif response > number:
    print('Sorry, too high. The number was ' + str(number))
else:
    print('Correct! The number was ' + str(number))
