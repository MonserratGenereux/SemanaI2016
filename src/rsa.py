import utilities

def encode(message):
    fixedMessage = message.upper()
    for ch in utilities.fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')
    fixedMessage = map(lambda x: ord(x) - 64 if x != ' ' else 0 , list(fixedMessage))
    encodedMessage = []
    for x in range(len(fixedMessage) / 2):
        encodedMessage.append(fixedMessage[2 * x] * 27 + fixedMessage[2 * x + 1])
    return encodedMessage

def decode(encodedMessage):
    fixedMessage = []
    for e in encodedMessage:
        fixedMessage.append(e / 27)
        fixedMessage.append(e % 27)
    return "".join(map(lambda x: chr(x + 64) if x > 0 else ' ', fixedMessage))

def cipher(message, publicKey):
    fixedMessage = encode(message)
    return map(lambda x: utilities.powerMod(x, publicKey[1], publicKey[0]), fixedMessage)

def decipher(message, privateKey):
    fixedMessage = map(lambda x: utilities.powerMod(x, privateKey[1], privateKey[0]), message)
    return decode(fixedMessage)
