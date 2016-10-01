import utilities

def cipher(message, key):
    fixedMessage = message.upper()
    fixedKey = key.upper()
    for ch in utilities.fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')
        fixedKey = fixedKey.replace(ch, '')

    asciiCode = map(lambda x: x - 65, map(ord, list(fixedMessage)))
    for x in range(0, len(asciiCode)):
        asciiCode[x] = (asciiCode[x] + (ord(fixedKey[x % len(fixedKey)]) - 65)) % 26
    asciiCode = map(lambda x: chr(x + 65), asciiCode)
    return "".join(asciiCode)

def decipher(message, key):
    fixedMessage = message.upper()
    fixedKey = key.upper()
    for ch in utilities.fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')
        fixedKey = fixedKey.replace(ch, '')

    asciiCode = map(lambda x: x - 65, map(ord, list(fixedMessage)))
    for x in range(0, len(asciiCode)):
        asciiCode[x] = (asciiCode[x] - (ord(fixedKey[x % len(fixedKey)]) - 65)) % 26
    asciiCode = map(lambda x: chr(x + 65), asciiCode)
    return "".join(asciiCode)
