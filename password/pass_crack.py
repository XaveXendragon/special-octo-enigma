#pass_crack

import random, openpyxl


    
core = openpyxl.Workbook()
sheet = core.active
sheet.title = "DATA"
row = 1
col = 1
    
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
s123 = "0123456789"
test = "0418Freedom"

flag = True
counter = 0

def write(guess):
    global row
    global col
    sheet.cell(row, col, guess)
    row += 1
    if row >= 51:
        col += 1
        row = 1
        
#def plant():
#    while col <= num_col:
#        gen_data()
#        counter = 1
#        col += 1

def gene(length):
    passw = []
    for x in range(length):
        ran_a = random.choice(abc)
        ran_A = random.choice(ABC)
        ran_123 = random.choice(s123)
#The line below, is a source of failure when generating a password, 
#because it's picking a character at random. Additional code is needed to
#narrow the choice after each choice is made.    
        rule = [ran_a, ran_A, ran_123]
        passw.append(random.choice(rule))
    return "".join(passw)
#        return "1234"

def check(passw, guess):
    print("Guess: " + guess)
    global counter
    global flag
    counter += 1    
    print("Try: " + str(counter))
    if guess == passw:
        print ("Boom")
        flag = False
    else:
        print ("Sorry")
        write(guess)

def gogo():
    while flag is True:
        print ("Computer: " + test)
        check(test, gene(11))

gogo()
core.save("core.xlsx")
