import re

instructions = input()
desert_map = {}
directions = ["L", "R"]

input()
while True:
    user_input = input()
    if not user_input:
        break
    node, left, right = re.findall('\w+', user_input)
    desert_map[node] = desert_map.get(node, (left, right))

current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    current_node = desert_map[current_node][directions.index(instructions[steps % len(instructions)])]
    steps += 1
print(steps)
