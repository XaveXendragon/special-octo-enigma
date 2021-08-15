#Guess CvC Ver V (No Love)

import random

myguess = 7777

bank = []
tries = -1
dup = 0

def guess():
    guess = random.randint(1, 9999)
    return guess

def check(guess):
    global dup
    if guess in bank:
#        print(guess)
        dup += 1
    else:
#        print("No")
        bank.append(guess)

def main():
    while True:
        cg = guess()
        global tries
        tries += 1
        if cg == myguess:
            print("Congrats!!! "+ str(tries) + " tries")
            break
        else:
            check(cg)
            
main()

print("Duplicate guess: " + str(dup))
print("Good guess: " + str(len(bank)))
#print(bank)