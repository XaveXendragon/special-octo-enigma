# pass_crack V2

import random

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
s123 = "0123456789"
test = "123abc"

flag = True
counter = 0
dup_c = 0

bank = []

def write_txt(guess):
    bank_file = open("bank.txt", "a+")
    bank_file.write(guess + ", ")
    bank_file.close()

def write_list(guess):
    bank.append(guess)

def read(guess):
    global dup_c
    bank_file= open("bank.txt")
    search = bank_file.read()
    if search.count(guess) == 0:
        print("No Dup")
    else:
        dup_c += 1
        print("Dup!!!")
        print(str(dup_c) + " dups!")
    bank_file.close()

def gene(length):
    passw = []
    for x in range(length):
        ran_a = random.choice(abc)
        ran_A = random.choice(ABC)
        ran_123 = random.choice(s123)
        # The line below, is a source of failure when generating a password,
        # because it's picking a character at random. Additional code is needed to
        # narrow the choice after each choice is made.
        rule = [ran_a, ran_A, ran_123]
        passw.append(random.choice(rule))
    return "".join(passw)

def check(passw, guess):
    print("Guess: " + guess)
    global counter
    global flag
#    read(guess)
    counter += 1
    print("Try: " + str(counter))
    if guess == passw:
        print("Boom")
        write_list(guess)
        flag = False
    else:
        print("Sorry")
        write_list(guess)


def run():
    while flag is True:
        print("Computer: " + test)
        check(test, gene(5))
    siz = len(bank)
    print(bank[siz - 1])

run()