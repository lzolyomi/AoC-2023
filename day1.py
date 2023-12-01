from helpers.fetch_data import split_lines
import re

# Path: Day1.py
DAY = 1

with open(f"data/day{DAY}.txt") as f:
    data = f.read()

# PART 1

pattern = r'\d'

total_sum = 0
lines = split_lines(data)
for line in lines:
    match = re.findall(pattern, line)
    first, last = match[0], match[-1]
    two_digit = int(first + last)
    total_sum += two_digit

print(f"PART 1 Total sum: {total_sum}")

# PART 2

converter = {"one":"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"n9e"}

total_sum = 0
lines = split_lines(data)
for line in lines:
    for key, value in converter.items():
        line = line.replace(key, value)
    match = re.findall(pattern, line)
    first, last = match[0], match[-1]
    if len(first) > 1:
        first = str(converter[first])
    if len(last) > 1:
        last = str(converter[last])
    two_digit = int(first + last)
    total_sum += two_digit

print(f"PART 2 Total sum: {total_sum}")