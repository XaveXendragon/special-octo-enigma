# pass_crack V3

import random

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
s123 = "0123456789"
test = "123abc"

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

print(gene(5))

def word():
    word = open("words_big.txt")
    word_read = word.readlines()
    word_list = []
    for x in word_read:
#        print(x)
        x = x.rstrip("\n")
        word_list.append(x)
#    print(word_list)