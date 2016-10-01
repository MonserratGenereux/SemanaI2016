import math

fixedChars = [',', '.', ':', ';']

def factorSemiPrime(n):
    for x in range(1, int(math.floor(math.sqrt(n)))):
        if n % (x + 1) == 0:
            return [x + 1, n / (x + 1)]
    return [1, n]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def getCriticalValues(valuesList):
    elements = [0] * 26
    for e in valuesList:
        elements[e] += 1
    values = [0, 0]
    for x in range(len(elements)):
        if elements[x] > elements[values[0]]:
            values[0] = x
        elif elements[x] > elements[values[1]]:
            values[1] = x
    return values

def powerMod(a, p, n, s = 0):
    r = 1
    for x in range(p):
        r = (r * a) % n
    return (r + s) % n

def splitMessage(message, n):
    result = []
    for x in range(n):
        result.append([])
    for x in range(len(message)):
        result[x % n].append(message[x])
    return result

def writeInputToFile(possibleResults, filename):
    f = open(filename, 'w')
    for e in possibleResults:
        f.write(str(e[0]) + '\n')
        f.write(str(e[1]) + '\n')
        f.write('\n')
    f.close()
    print "Possible solutions printed in file " + filename

# Base code from xgcd taken from https://goo.gl/5TrU8E
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0
