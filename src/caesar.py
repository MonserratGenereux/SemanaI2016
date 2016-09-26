fixedChars = [',', '.', ':', ';', ' ']

def encode(message, key):
    fixedMessage = message.upper()
    for ch in fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')

    asciiCode = map(lambda x: x - 65, map(ord, list(fixedMessage)))
    asciiCode = map(lambda x: (x + (ord(key.upper()) - 65)) % 26, asciiCode)
    asciiCode = map(chr, map(lambda x: x + 65, asciiCode))
    return "".join(asciiCode)

def decode(message, key):
    fixedMessage = message.upper()
    for ch in fixedChars:
        fixedMessage = fixedMessage.replace(ch, '')

    asciiCode = map(lambda x: x - 65, map(ord, list(fixedMessage)))
    asciiCode = map(lambda x: (x - (ord(key.upper()) - 65)) % 26, asciiCode)
    asciiCode = map(chr, map(lambda x: x + 65, asciiCode))
    return "".join(asciiCode)
