import vigenere
import itertools

def splitMessage(message, n):
    result = []
    for x in range(n):
        result.append([])
    for x in range(len(message)):
        result[x % n].append(message[x])
    return result

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

def buildKeys(listOfCriticalValues):
    fixedKeys = list(itertools.product(*listOfCriticalValues))
    keys = []
    for t in fixedKeys:
        keys.append("".join(map(lambda x: chr((x - 4) % 26 + 65), t)))
    return keys

def main(message, maxKeyLength):
    fixedMessage = map(lambda x: ord(x) - 65, list(message))
    keys = []
    for x in range(maxKeyLength):
        messageLists = splitMessage(fixedMessage, x + 1)
        criticalValues = []
        for y in range(len(messageLists)):
            criticalValues.append(getCriticalValues(messageLists[y]))
        tempKeys = buildKeys(criticalValues)
        for e in tempKeys:
            keys.append(e)
    return keys

def writeInputToFile(keys, message, fileName):
    f = open(fileName, 'w')
    for k in keys:
        f.write(k + '\n')
        f.write(vigenere.decode(message, k) + '\n')
        f.write('\n')
    f.close()

aFile = 'output.txt'
aMessage = "LEIDGVLFRJCYXCUFHVHUJDUDRKIDVVUOKIIFRIXDXDIRWYYNRDVQKRXFZFWAPGFQWVMQWJIRFFHFDTNEREYRRICZSLNFRNUDGJNTHIYROVWFRIUZGKBQRKBQUWIDRLNBXKZDRDNTHIYROVWFRIMAWYUFWYYDHWFQFKYPVZAZDCWAXCXBDJMNDTEFKIIGJYUEHGUDDKYEHKIRFFHFDTNEHRWTGIOYKRXAQVBGQULQGRHPIFODZZLQEIOEKVMIKZWTPRXQFFHFDTNILKBFKVJXDKYAQKIIKZWTWYYKZVLQOFUPHUNTHSLGVYYEDEXFKVWAUIYESFHPLEAEHKIRFFHFDTNERENTHGFMWVQQUVUDURHSHUCZIFODFFHOHENDLTWUUTFQVFZFZVHFBJCJWYYAXKYDSRCDRWWUUTFQVZHBXKUZGFOFSLNIHIYQTLCHDCYZWKIFKVWGUIYZWZHMQVHUJDUBDJMUQXCZREYPLIYOWZIZWYLAXXBFKVMOURGNOVLMQUNTHZHZHIJMLIYCXZPMOVHFWFNTHTODUVHFICIILEAUQKBQRGJAVZNQGZLQFKCAQ"
writeInputToFile(main(aMessage, 6), aMessage, aFile)
