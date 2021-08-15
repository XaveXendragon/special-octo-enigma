#Not my code again

import time

DIGITS = 15000

def pi_digits(x):
    """Generate x digits of Pi."""
    k,a,b,a1,b1 = 2,4,1,12,4
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1
t0 = time.time()
digits = [str(n) for n in list(pi_digits(DIGITS))]
t1 = time.time() - t0
print("%s.%s\n" % (digits.pop(0), "".join(digits)))
print(t1)