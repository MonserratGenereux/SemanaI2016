import rsa
import shor
import utilities

def breakCipher(publicKey, useShor = False):
    if useShor:
        pq = shor.factorSemiPrime(publicKey[0])
    else:
        pq = utilities.factorSemiPrime(publicKey[0])
    t = (pq[0] - 1) * (pq[1] - 1)
    return utilities.xgcd(publicKey[1], t) % t
