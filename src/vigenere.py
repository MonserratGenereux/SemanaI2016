fixedChars = [',', '.', ':', ';', ' ']

def encode(message, key):
    fixedMessage = message.upper()
    fixedKey = key.upper()
    for ch in fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')
        fixedKey = fixedKey.replace(ch, '')

    asciiCode = map(lambda x: x - 65, map(ord, list(fixedMessage)))
    for x in range(0, len(asciiCode)):
        asciiCode[x] = (asciiCode[x] + (ord(fixedKey[x % len(fixedKey)]) - 65)) % 26
    asciiCode = map(chr, map(lambda x: x + 65, asciiCode))
    return "".join(asciiCode)

def decode(message, key):
    fixedMessage = message.upper()
    fixedKey = key.upper()
    for ch in fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')
        fixedKey = fixedKey.replace(ch, '')

    asciiCode = map(lambda x: x - 65, map(ord, list(fixedMessage)))
    for x in range(0, len(asciiCode)):
        asciiCode[x] = (asciiCode[x] - (ord(fixedKey[x % len(fixedKey)]) - 65)) % 26
    asciiCode = map(chr, map(lambda x: x + 65, asciiCode))
    return "".join(asciiCode)
