line1 = '.' * 142
line2 = '.' + input() + '.'
line3 = '.' + input() + '.'

part_numbers = []

while True:

    isPart = False
    currNum = -1
    index = 0

    for char in line2:
        if char.isdigit():
            for i in range(-1, 2):
                if (not line1[index + i].isdigit() and not line1[index + i].isalpha() and line1[index + i] != "." or
                        not line3[index + i].isdigit() and not line3[index + i].isalpha() and line3[index + i] != "." or
                        not line2[index + i].isdigit() and not line2[index + i].isalpha() and line2[index + i] != "."
                ):
                    isPart = True
            if currNum == -1:
                currNum = int(char)
            else:
                currNum = int(str(currNum) + char)
        if not char.isdigit() and currNum != -1 and isPart:
            part_numbers.append(currNum)
            print(currNum)
            currNum = -1
            isPart = False
        elif not char.isdigit() and currNum != -1 and not isPart:
            currNum = -1
            isPart = False
        index += 1
    if line3 == '..............................................................................................................................................':
        print(sum(part_numbers))
    line1 = line2
    line2 = line3
    line3 = '.' + input() + '.'
    currNum = -1
