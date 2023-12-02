import re

DAY = 2

with open(f"data/day{DAY}.txt") as f:
    data = f.read()

# PART 1

def is_valid(draws):
    limits = {"blue":14, "green":13, "red":12}
    return all([int(draw[0]) <= limits[draw[1]] for draw in draws])

def part1(data):
    sum_valid = 0
    lines = data.split("\n")
    for line in lines:
        id_pattern = r'Game (\d+)'
        games_pattern = r'(\d+) (green|blue|red)'
        id = re.findall(id_pattern, line)
        assert len(id) == 1, "id should be unique"
        draws = re.findall(games_pattern, line)
        if is_valid(draws):
            sum_valid += int(id[0]) 
    print(f"PART 1 Total sum: {sum_valid}")
part1(data)

# PART 2

def minimum_cubes(draws):
    minimums = {"blue":0, "green":0, "red":0}
    for draw in draws:
        color = draw[1]
        if int(draw[0]) > minimums[color]:
            minimums[color] = int(draw[0])
    return minimums

def part2(data):
    sum_powers = 0
    lines = data.split("\n")
    for line in lines:
        id_pattern = r'Game (\d+)'
        games_pattern = r'(\d+) (green|blue|red)'
        id = re.findall(id_pattern, line)
        assert len(id) == 1, "id should be unique"
        draws = re.findall(games_pattern, line) 
        minimums = minimum_cubes(draws)
        power  = 1
        for minimum in minimums.values():
            power *= minimum
        sum_powers += power
    print(f"PART 2 Total sum: {sum_powers}")

part2(data)