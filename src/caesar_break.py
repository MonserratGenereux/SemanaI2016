import caesar
import utilities

def breakCipher(message):
    possibleSolutions = []
    for x in range(26):
        key = chr(x + 65)
        possibleSolutions.append([key, caesar.decipher(message, key)])
    return possibleSolutions
