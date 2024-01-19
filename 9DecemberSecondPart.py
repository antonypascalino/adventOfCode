import re

total_sum = 0
while True:
    user_input = input()
    if not user_input:
        break
    sequence = list(map(int, re.findall('-?\d+', user_input)))
    next_sequence = []
    first_ones = []
    while True:
        for index, number in enumerate(list(sequence)):
            if index + 1 < len(sequence):
                next_sequence.append(sequence[index+1] - number)
        print(sequence)
        first_ones.append(sequence[0])
        if all(element == 0 for element in next_sequence):
            break
        sequence = next_sequence
        next_sequence = []

    first_summed = 0
    for number in range(len(first_ones) - 1, -1, -1):
        first_summed = first_ones[number] - first_summed

    total_sum += first_summed

print(total_sum)




