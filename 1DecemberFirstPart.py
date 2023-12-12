
calValues = []
while True:
    user_input = input()

    isFirst = True
    firstDigit = -1
    lastDigit = -1

    for char in user_input:
        if char.isdigit():
            num = int(char)
            if isFirst:
                firstDigit = num
                isFirst = False
            else:
                lastDigit = num
    if lastDigit == -1:
        lastDigit = firstDigit
    calValue = int(str(firstDigit) + str(lastDigit))
    calValues.append(calValue)
    total = sum(calValues)
    print(total)

