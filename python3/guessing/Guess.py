#Guessing game

import random

print("Guess what number the computer is thinking of, 1 - 100?")

computer = random.randint(1, 100)
#print("Cheater " + str(computer))
counter = 0

while True:
    guess = int(input('Your guess? '))
    counter = counter + 1
    if guess == computer:
        print('Good guess!!!')
        print (str(counter) + " tries")
        break
    elif guess < computer:
        print('Too low')
    elif guess > computer:
        print('Too high')
