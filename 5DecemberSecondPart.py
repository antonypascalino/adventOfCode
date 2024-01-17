def get_map(puzzle_map):
    while True:
        puzzle_input = input()
        if puzzle_input == "":
            break

        curr_line = []
        curr_number = ""
        for character in puzzle_input:
            if character == " ":
                curr_line.append(int(curr_number))
                curr_number = ""
            elif character.isdigit():
                curr_number += character
        curr_line.append(int(curr_number))
        puzzle_map.append(curr_line)


def find_mapped_value(seed_range, current_map):
    for line in current_map:
        source, dest, length = map(int, line.split(" "))
        x1, x2 = map(int, seed_range)
        end = dest + length
        diff = end - dest
        if x2 <= dest and x1 >= end:
            find_mapped_value((x1+diff, x2+diff), current_map)
        if x1 > dest and x2 < end:
            x1 = x1 + diff
            x2 = x2 + diff
        if x1 < dest:
            find_mapped_value((x1, dest), current_map)
        if x2 > end:
            find_mapped_value((end, x2), current_map)


user_input = input()
user_input = user_input.split(":")[1]
seeds_ranges = []

curr_seed = ""
curr_range = ""
isSeed = True
firstBlank = True

# Read all the seed integers
for char in user_input:
    if char.isdigit():
        if isSeed:
            curr_seed += char
        else:
            curr_range += char
    if char == " " and firstBlank:
        firstBlank = False
    elif char == " " and not firstBlank:
        if isSeed:
            curr_seed = int(curr_seed)
            isSeed = False
        else:
            curr_range = int(curr_range)
            seeds_ranges.append((curr_seed, curr_seed + curr_range))
            curr_seed = ""
            curr_range = ""
            isSeed = True
curr_range = int(curr_range)
seeds_ranges.append((curr_seed, curr_seed + curr_range))
print(seeds_ranges)

input()
input()
seed_to_soil_map = []
get_map(seed_to_soil_map)

input()
soil_to_fertilizer_map = []
get_map(soil_to_fertilizer_map)

input()
fertilizer_to_water_map = []
get_map(fertilizer_to_water_map)

input()
water_to_light_map = []
get_map(water_to_light_map)

input()
light_to_temperature_map = []
get_map(light_to_temperature_map)

input()
temperature_to_humidity_map = []
get_map(temperature_to_humidity_map)

input()
humidity_to_location_map = []
get_map(humidity_to_location_map)

locations = []
for seed in seeds:
    print(seed)
    soil = find_mapped_value(seed, seed_to_soil_map)
    fertilizer = find_mapped_value(soil, soil_to_fertilizer_map)
    water = find_mapped_value(fertilizer, fertilizer_to_water_map)
    light = find_mapped_value(water, water_to_light_map)
    temperature = find_mapped_value(light, light_to_temperature_map)
    humidity = find_mapped_value(temperature, temperature_to_humidity_map)
    location = find_mapped_value(humidity, humidity_to_location_map)

    locations.append(location)

print(min(locations))
