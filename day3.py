import numpy as np

# DAY 3
DAY = 3

# Read data

with open(f"data/day{DAY}.txt", "r") as f:
    lines = f.readlines()

n, m = len(lines), len(lines[0]) -1
data = np.zeros((n, m), dtype=np.object_)
for idx, line in enumerate(lines):
    data[idx] = [*line.strip()]

# PART 1

def discover_numbers(i, j):
    # return sum of all surrounding numbers
    total = 0
    # check surrounding elements if numeric, and if so, discover all digits to get the whole number
    idx_to_check = [(i-x, j-y) for x in range(-1, 2) for y in range(-1, 2)]
    idx_checked = {x: False for x in idx_to_check}
    for x in idx_to_check:
        if not idx_checked[x]:
            idx_checked[x] = True
            row, col = x # unpack tuple
            if data[row, col].isnumeric():
                number = data[row, col] # will add to begin/end depending on
                # check both to left and right
                start = col
                while data[row, col-1].isnumeric():
                    number = data[row, col-1] + number
                    idx_checked[(row, col-1)] = True
                    if col == 0:
                        break
                    col -= 1
                col = start
                while data[row, col+1].isnumeric():
                    number += data[row, col+1]
                    idx_checked[(row, col+1)] = True
                    col += 1
                    if col == m-1:
                        break
                total += int(number)

    return total
            
result = 0
for i in range(n):
    for j in range(m):
        # if data[i, j] not numeric or not a dot
        if (not data[i, j].isnumeric()) and (data[i, j] != "."):
            # check surrounding elements if numeric
            result += discover_numbers(i, j)
print(f"Part 1: {result}")

# PART 2

def discover_numbers(i, j):
    # check surrounding elements if numeric, and if so, discover all digits to get the whole number
    idx_to_check = [(i-x, j-y) for x in range(-1, 2) for y in range(-1, 2)]
    idx_checked = {x: False for x in idx_to_check}
    # check if exactly 2 numbers are adjacent, 
    num_adjacent_numbers = 0
    adjacent_numbers = []
    for x in idx_to_check:
        if not idx_checked[x]:
            idx_checked[x] = True
            row, col = x # unpack tuple
            if data[row, col].isnumeric():
                num_adjacent_numbers += 1
                if num_adjacent_numbers > 2:
                    return 0
                number = data[row, col] # will add to begin/end depending on
                # check both to left and right
                start = col
                while data[row, col-1].isnumeric():
                    number = data[row, col-1] + number
                    idx_checked[(row, col-1)] = True
                    if col == 0:
                        break
                    col -= 1
                col = start
                while data[row, col+1].isnumeric():
                    number += data[row, col+1]
                    idx_checked[(row, col+1)] = True
                    col += 1
                    if col == m-1:
                        break
                adjacent_numbers.append(int(number))
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    else:
        return 0
            
result = 0
for i in range(n):
    for j in range(m):
        # if data[i, j] not numeric or not a dot
        if data[i, j] == "*":
            # check if exactly 2 numbers are adjacent, multiply them and return the product
            result += discover_numbers(i, j)
print(f"Part 2: {result}")