import rsa
import rsa_break

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

for x in range(6):
    currentPrivateKey = [publicKeys[x][0], rsa_break.breakCipher(publicKeys[x])]
    print "Team " + str(x + 1)
    print "Private key: " + str(currentPrivateKey)
    print "Message: " + str(rsa.decipher(messages[x], currentPrivateKey))
    print
