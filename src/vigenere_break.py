import itertools
import utilities
import vigenere

def buildKeys(listOfCriticalValues):
    fixedKeys = list(itertools.product(*listOfCriticalValues))
    keys = []
    for t in fixedKeys:
        keys.append("".join(map(lambda x: chr((x - 4) % 26 + 65), t)))
    return keys

def breakCipher(message, maxKeyLength, minKeyLength = 1):
    fixedMessage = map(lambda x: ord(x) - 65, list(message))
    results = []
    for x in range(minKeyLength, maxKeyLength + 1):
        messageLists = utilities.splitMessage(fixedMessage, x)
        criticalValues = []
        for y in range(len(messageLists)):
            criticalValues.append(utilities.getCriticalValues(messageLists[y]))
        tempKeys = buildKeys(criticalValues)
        for key in tempKeys:
            results.append([key, vigenere.decipher(message, key)])
    return results
