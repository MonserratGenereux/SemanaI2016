import sys
sys.path.insert(1, '../src')

import rsa
import rsa_break
import utilities

publicKeys = [[1003, 347],
              [1007, 335],
              [1037, 229],
              [1081, 227],
              [1211, 299],
              [1159, 367]]

messages = [[264, 702, 224, 329, 951],
            [523, 438, 642, 542, 184],
            [945, 807, 704, 651, 588],
            [849, 47, 410, 92, 1014],
            [525, 16, 940, 513, 816],
            [302, 187, 1013, 425, 943]]

results = []
filename = "rsa_output.txt"
for x in range(len(publicKeys)):
    tempKey = [publicKeys[x][0], rsa_break.breakCipher(publicKeys[x])]
    results.append(["Key: " + str(tempKey) + "\nMessage: " + str(messages[x]), rsa.decipher(messages[x], tempKey)])

utilities.writeInputToFile(results, filename)
