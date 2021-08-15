import math

print("Is it Prime")

n = int(input("Enter Number: "))

if n < 2:
    print ("All Prime numbers are greater that 1")
    quit()
elif n == 2:
    print("It's Prime")
    quit()
    
i = 2

limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("It's not Prime")
        quit()
    i += 1
    
print ("It's Prime")