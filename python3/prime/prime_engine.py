# Running module

import prime

bank = []

for x in range(3, 500000):
    ccheck = prime.prime(x)
    if ccheck != "It's not Prime":
        bank.append(x)

print(bank)
