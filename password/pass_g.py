#Generate a password, based in rules

import random

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
s123 = "0123456789"

abc_list = list(abc)
ABC_list = list(ABC)
s123_list = list(s123)

abc_conv = []
ABC_conv = []
s123_conv = []

for x in abc_list:
    conv = ord(x)
    abc_conv.append(conv)
for x in ABC_list:
    conv = ord(x)
    ABC_conv.append(conv)
for x in s123_list:
    conv = ord(x)
    s123_conv.append(conv)

_pass = []
_pass_ = []

u_input = int(input("Enter the number of char in your random password: "))

while u_input > 0:
    ran_a = random.choice(abc_conv)
    ran_A = random.choice(ABC_conv)
    ran_123 = random.choice(s123_conv)
#The line below, is a source of failure when generating a password, 
#because it's picking a character at random. Additional code is needed to
#narrow the choice after each choice is made.    
    rule = [ran_a, ran_A, ran_123]
    _pass.append(random.choice(rule))
    u_input -= 1

for x in _pass:
    conv = chr(x)
    _pass_.append(conv)

pass_g_output = "".join(_pass_)
#print(pass_g_output)
