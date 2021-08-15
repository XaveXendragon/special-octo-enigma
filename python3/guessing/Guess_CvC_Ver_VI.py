#Guess CvC Ver VI (now with remove!!!)

import random

source = []
effi_list = []

def gene(low, high):
    for x in range(low, high):
        source.append(x)

def guess1():
    guess = random.choice(source)
    return guess

def guess2():
    guess = random.choice(source)
    source.remove(guess)
    return guess

def main():
    gene(1, 100001)
    global effi
    computer1 = guess1()
    computer2 = guess2()
    while True:
        if computer2 == computer1:
            print("Comgrats!!! Your guessed correctly: " + str(computer2))
            print("Only " + str(len(source)) + " guesses left")
            effi = round(len(source)/100000 * 100, 2)
            print("Efficiency: " + str(effi) + "%")
            break
        else:
            computer2 = guess2()
    
main()