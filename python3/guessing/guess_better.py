import random

the_number = random.randint(1, 1000)
guess = -1
tries = 1

lower_bound = 1
higher_bound = 1000

while guess != the_number:
    guess = int(input("Take a guess: "))
    tries += 1
    if guess > the_number:
        print("Lower!\n")
    elif guess < the_number:
        print("Higher!\n")
    else:
        break
    cg = random.randint(lower_bound, higher_bound)
    print("The computer guessed: " + str(cg))
    tries += 1
    if cg > the_number:
        higher_bound = cg - 1
        print("Too high Computer.\n")
    elif cg < the_number:
        lower_bound = cg + 1
        print("Too low Computer.\n")
    else:
        break