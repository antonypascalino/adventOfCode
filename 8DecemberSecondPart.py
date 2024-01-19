import re
import math

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

current_nodes = {key: value for key, value in desert_map.items() if starting_pattern.search(key)}
total_steps = []

for node, value in list(current_nodes.items()):
    steps = 0
    while node[2] != "Z":
        node = desert_map[node][directions.index(instructions[steps % len(instructions)])]
        steps += 1
    print(node)
    total_steps.append(steps)

print(math.lcm(*total_steps))


