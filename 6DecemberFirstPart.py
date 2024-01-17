import re
import math

times = re.findall('(\d+)', input().split(":")[1])
distances = re.findall('(\d+)', input().split(":")[1])
races = list(zip(map(int, times), map(int, distances)))
print(races)

wins = []
for race in races:
    beat = 0
    for velocity in range(1, race[0]):
        run_time = race[0] - velocity
        distance = run_time * velocity
        if distance > race[1]:
            beat += 1
        elif beat > 0:
            break
    wins.append(beat)

print(math.prod(wins))







