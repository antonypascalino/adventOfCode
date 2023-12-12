calValues = []
wordDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

while True:
    user_input = input()

    isFirst = True
    firstDigit = -1
    lastDigit = -1
    potentialNumber = ""

    for char in user_input:
        if char.isdigit():
            num = int(char)
            if isFirst:
                firstDigit = num
                isFirst = False
            else:
                lastDigit = num
            potentialNumber = ""
        else:
            potentialNumber += char
            for word in wordDigits:
                if word in potentialNumber:
                    num = wordDigits.index(word) + 1
                    if isFirst:
                        firstDigit = num
                        isFirst = False
                    else:
                        lastDigit = num
                    potentialNumber = ""
    if lastDigit == -1:
        lastDigit = firstDigit
    calValue = int(str(firstDigit) + str(lastDigit))
    calValues.append(calValue)
    total = sum(calValues)
    print(total)

