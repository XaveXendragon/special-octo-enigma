#Create a module for finding primes

import math


def prime(n):
    if n < 2:
        return("All Prime numbers are greater than 1")
    elif n == 2:
        return("It's Prime")
    
    i = 2

    limit = int(math.sqrt(n))

    while i <= limit:
        if n % i == 0:
            return("It's not Prime")
            #quit()
        i += 1
    
    return("It's Prime")