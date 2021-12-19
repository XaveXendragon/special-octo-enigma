# Kaprekar's Constant

from random import randint as ri
from sys import exit

print("""Kaprekar's Constant:
Take almost any 4 digit number
Reorder it from largest to smallest
Then reorder it from smallest to largest
Subtract the smaller number from the large number
If you keep doing this, you'll always end with the number 6174""")
_input = input("Enter any 4 digit number: ")
if int(_input) < 1000:
        print("It's got to be a 4 digit number")
        exit()

def work(x):
    x = str(x)
    if len(x) == 4:
        return x
    elif len(x) == 3:
        x = str(0) + x
        return x
    elif len(x) == 2:
        x = str(00) + x
        return str(x)
    elif len(x) == 1:
        x = str(000) + x
        return x
    else:
        print("WHAT!!!")
        return str(0000)

def work_l(x):
    x = str(x)
    if len(x) == 4:
        return str(x)
    elif len(x) == 3:
        x = str(0) + x
        return str(x)
    elif len(x) == 2:
        x = str(00) + x
        return str(x)
    elif len(x) == 1:
        x = str(000) + x
        return str(x)
    else:
        print("WHAT!!!")
        return str(0000)

def work_r(x):
    x = str(x)
    if len(x) == 4:
        return str(x)
    elif len(str(x)) == 3:
        x = x + str(0)
        return str(x)
    elif len(x) == 2:
        x = x + str(00)
        return str(x)
    elif len(x) == 1:
        x = x + str(000)
        return str(x)
    else:
        print("WHAT!!!")
        return str(0000)

def conv(x):
    unsorted = list(str(x))
    s_l = sorted(unsorted, reverse=False)
    s_lj = "".join(s_l)
    s_lj = work_l(s_lj)
    print(s_lj)
    l_s = sorted(unsorted, reverse=True)
    l_sj = "".join(l_s)
    l_sj = work_r(l_sj)
    print(l_sj)
    done = int(l_sj) - int(s_lj)
    done = work(done)
    return str(done)

while True:
    _input = int(_input)
    if _input == 6174:
        print("It's a Kapre!!!")
        break
    elif _input == 0:
        print("Not a Kapre, must be number that's the same front to back")
        break
    else:
        _input = conv(_input)