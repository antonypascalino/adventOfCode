# line1 = '.' * 16
# line2 = '...' + input() + '...'
# line3 = '...' + input() + '...'

line1 = '.' * 146
line2 = '...' + input() + '...'
line3 = '...' + input() + '...'

part_numbers_sum = 0


class Number:

    def __init__(self, digits, is_adjacent):
        self.digits = digits
        self.is_adjacent = is_adjacent

    def add_digit(self, digit, is_adjacent):
        self.digits += digit
        if is_adjacent:
            self.is_adjacent = True

    def get_value(self):
        value = ""
        for digit in self.digits:
            value += digit
        return int(value)

    def adjacent(self):
        return self.is_adjacent


while True:

    index = 0

    for char in line2:
        if char == '*':

            numbers = []

            num = None
            for i in range(-3, 4):
                if line1[index+i].isdigit():
                    if num is None:
                        num = Number(line1[index+i], -1 <= i <= 1)
                    else:
                        num.add_digit(line1[index+i], -1 <= i <= 1)
                else:
                    if num is not None:
                        if num.adjacent():
                            numbers.append(num.get_value())
                        num = None
            if num is not None and num.adjacent():
                numbers.append(num.get_value())
                num = None

            num = None
            for i in range(-3, 4):
                if line3[index+i].isdigit():
                    if num is None:
                        num = Number(line3[index+i], -1 <= i <= 1)
                    else:
                        num.add_digit(line3[index+i], -1 <= i <= 1)
                else:
                    if num is not None:
                        if num.adjacent():
                            numbers.append(num.get_value())
                        num = None
            if num is not None and num.adjacent():
                numbers.append(num.get_value())
                num = None

            num = None
            for i in range(-3, 4):
                if line2[index+i].isdigit():
                    if num is None:
                        num = Number(line2[index+i], -1 <= i <= 1)
                    else:
                        num.add_digit(line2[index+i], -1 <= i <= 1)
                else:
                    if num is not None:
                        if num.adjacent():
                            numbers.append(num.get_value())
                        num = None
            if num is not None and num.adjacent():
                numbers.append(num.get_value())
                num = None

            if numbers.__len__() == 2:
                part_numbers_sum += numbers[0] * numbers[1]
                print(part_numbers_sum)

        index += 1

    line1 = line2
    line2 = line3
    line3 = '...' + input() + '...'










