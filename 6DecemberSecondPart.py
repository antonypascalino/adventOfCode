import re
import functools


def find_win(start, end, step):
    for velocity in range(start, end, step):
        run_time = time - velocity
        distance = run_time * velocity
        if distance > record_distance:
            return velocity


time = int(functools.reduce(lambda x1,x2: x1 + x2, re.findall('(\d)', input().split(":")[1])))
record_distance = int(functools.reduce(lambda x1,x2: x1 + x2, re.findall('(\d)', input().split(":")[1])))

print(find_win(time, 1, -1) - find_win(1, time, 1) + 1)
