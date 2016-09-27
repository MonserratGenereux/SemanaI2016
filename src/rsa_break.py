import rsa

# Base code from gcd taken from https://goo.gl/5TrU8E
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0

def factorPrimes(p):
    for x in range(2, p):
        if p % x == 0:
            return [x, p / x]
    return -1

def breakCipher(publicKey):
    pq = factorPrimes(publicKey[0])
    t = (pq[0] - 1) * (pq[1] - 1)
    return xgcd(publicKey[1], t) % t
