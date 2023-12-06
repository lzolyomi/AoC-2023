from math import sqrt, ceil, floor
import re

DAY = 6

# Parse data
with open(f"data/day{DAY}.txt", "r") as f:
    data = f.read().splitlines()
    pattern = r"(\d+)"
    times = [int(match) for match in re.findall(pattern, data[0].split(":")[1].strip())]
    records = [int(match) for match in re.findall(pattern, data[1].split(":")[1].strip())]

# part 1

def calculate_ways_to_win(time, record):
    # Calculate the discriminant of the quadratic equation
    delta = time**2 - 4 * record

    # Calculate the number of ways to beat the record
    ways = ceil((time + sqrt(delta)) / 2 - 1) - floor((time - sqrt(delta)) / 2 + 1) + 1
    return ways

# Calculate the total number of ways to win all races
mulnumbers = 1
for time, record in zip(times, records):
    mulnumbers *= calculate_ways_to_win(time, record)

print('Part 1:', mulnumbers)

# part 2

# create single number from list of numbers, both for times and records
times_str = int(''.join([str(x) for x in times]))
records_str = int(''.join([str(x) for x in records]))

print('Part 2:', calculate_ways_to_win(times_str, records_str))