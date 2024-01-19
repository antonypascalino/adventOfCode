import re

total_sum = 0
while True:
    user_input = input()
    if not user_input:
        break
    sequence = list(map(int, re.findall('-?\d+', user_input)))
    next_sequence = []
    last_ones = []
    while True:
        for index, number in enumerate(list(sequence)):
            if index + 1 < len(sequence):
                next_sequence.append(sequence[index+1] - number)
            else:
                last_ones.append(number)
        print(sequence)
        if all(element == 0 for element in next_sequence):
            break
        sequence = next_sequence
        next_sequence = []

    lasts_summed = 0
    for number in range(len(last_ones) - 1, -1, -1):
        print(last_ones[number], end=" + ")
        lasts_summed += last_ones[number]
    print("\n", lasts_summed)
    total_sum += lasts_summed

print(total_sum)




