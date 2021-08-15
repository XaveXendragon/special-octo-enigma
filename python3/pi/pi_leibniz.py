#Calculating pi with a Leibniz's series (not my code)
# 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

# Initialize denominator
k = 1

# Initialize sum
s = 0

for i in range(1000000):

    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
        #print(s)
    else:

        # odd index elements are negative
        s -= 4/k
        #print(s)

    # denominator is odd
    k += 2
    
print(s)