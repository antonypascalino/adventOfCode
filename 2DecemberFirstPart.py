currGame = 1
possibleGames = []

while True:

    maxBlu = 0
    maxGreen = 0
    maxRed = 0

    user_input = input()
    if user_input == "STOP":
        break
    user_input = user_input.split(":",1)[-1]
    currNum = 0
    isFirstDigit = True
    previousWasSpace = False

    for char in user_input:

        if char.isdigit():
            if isFirstDigit:
                currNum = int(char)
                isFirstDigit = False
            else:
                currNum = int(str(currNum) + char)
                isFirstDigit = True

        elif char == "b":
            if currNum > maxBlu:
                maxBlu = currNum
                currNum = 0

        elif char == "g":
            if currNum > maxGreen:
                maxGreen = currNum
                currNum = 0

        elif char == "r" and previousWasSpace:
            if currNum > maxRed:
                maxRed = currNum
                currNum = 0

        elif char == " ":
            previousWasSpace = True
            isFirstDigit = True

    print(maxBlu, maxGreen, maxRed)
    if maxRed <= 12 and maxGreen <= 13 and maxBlu <= 14:
        possibleGames.append(currGame)

    currGame += 1
    print(possibleGames)

print(sum(possibleGames))

