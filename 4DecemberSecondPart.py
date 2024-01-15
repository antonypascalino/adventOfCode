copies = {}
curr_card = 1

while True:

    user_input = input()

    if user_input == "":
        total_sum = sum(copies.values())
        print(total_sum)
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

    # print(str(winner_numbers) + " | " + str(current_numbers))

    current_points = 0

    copies[curr_card] = copies.get(curr_card, 0) + 1

    for number in current_numbers:
        if winner_numbers.__contains__(number):
            current_points += 1

    print(current_points)
    print("CURRENT CARD: " + str(curr_card))
    for i in range(1, current_points + 1, 1):
        copies[curr_card + i] = copies.get(curr_card + i, 0) + 1 * copies[curr_card]
    curr_card += 1

    print(copies)
