import math
import numpy
import random
import utilities

def getLocalMaxPositions(c):
    d = []
    for x in range(1, len(c) - 1):
        if c[x] > c[x - 1] and c[x] > c[x + 1]:
            d.append(x)
    return d

def factorSemiPrime(n):
    print "Calculating..."
    while True:
        a = random.randint(2, n - 1)
        if utilities.gcd(n, a) != 1 and n % a == 0:
            return [a, n / a]
        size = int(4 + 2**round(math.log(n, 2)))
        ax = map(lambda x: utilities.powerMod(a, x, n), range(size))
        c = map(numpy.absolute, numpy.fft.fft(ax))
        cLocalMaxPositions = getLocalMaxPositions(c)
        for e in cLocalMaxPositions:
            r = int((n / e))
            if r % 2 != 0:
                continue
            else:
                if utilities.powerMod(a, r / 2, n) == n - 1:
                    continue
                    p, q = gcd(utilities.powerMod(a, r / 2, n, 1), n), gcd(utilities.powerMod(a, r / 2, n, 1), n)
                    if p * q == n:
                        return [p, q]
