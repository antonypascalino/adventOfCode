total_points = 0

while True:

    user_input = input()
    if user_input == "":
        break

    user_input = user_input.split(":")[1]

    winner_input = user_input.split("|")[0]
    numbers_input = user_input.split("|")[1]

    winner_numbers = []
    current_numbers = []

    currNum = ""
    for index, char in enumerate(winner_input):
        if char.isdigit():
            if index == len(numbers_input) - 1 and currNum == "":
                winner_numbers.append(int(char))
            elif currNum == "":
                currNum = char
            else:
                currNum += char
                winner_numbers.append(int(currNum))
                currNum = ""
        else:
            if currNum != "":
                winner_numbers.append(int(currNum))
            currNum = ""

    for index, char in enumerate(numbers_input):
        if char.isdigit():
            if index == len(numbers_input) - 1 and currNum == "":
                current_numbers.append(int(char))
            elif currNum == "":
                currNum = char
            else:
                currNum += char
                current_numbers.append(int(currNum))
                currNum = ""
        else:
            if currNum != "":
                current_numbers.append(int(currNum))
            currNum = ""

    print(str(winner_numbers) + " | " + str(current_numbers))

    current_points = 0

    for number in current_numbers:
        if winner_numbers.__contains__(number):
            if current_points == 0:
                current_points = 1
            else:
                current_points *= 2

    print(current_points)
    total_points += current_points
    print(total_points)
