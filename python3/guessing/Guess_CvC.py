#Guessing game Computer1 vs Computer2

import random
import sys

print("Guessing Game Computer1 vs Computer2")
null_input = input("Press 'Enter' to GO")

computer1 = random.randint(1, 1000)
print("Computer1 picked " + str(computer1))

computer2 = random.randint(1,1000)
print("Computer2's first guess " + str(computer2))
counter = 0

while True:
    counter = counter + 1
    if computer2 == computer1:
        print("Good guess!!! " + str(computer2))
        print (str(counter) + " tries")
        break
    elif computer2 < computer1:
        print('Too low')
        computer2 = random.randint(computer2, 1000)
        
    elif computer2 > computer1:
        print('Too high')
        computer2 = random.randint(1, computer2)
sys.stdin.readline()