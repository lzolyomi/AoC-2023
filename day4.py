

DAY = 4

# Load data

with open(f"data/day{DAY}.txt", "r") as f:
    data = f.read().split("\n")


# Part 1

def part1(data):
    sum_points = 0
    for line in data:
        line = line.split(":")[1].strip()
        winning_numbers, present_numbers = line.split("|")
        winning_numbers = [int(x.replace(" ", "")) for x in winning_numbers.strip().split(" ") if x.isnumeric()]
        present_numbers = [int(x.replace(" ", "")) for x in present_numbers.strip().split(" ") if x.isnumeric()]
        winning_numbers = set(winning_numbers)
        present_numbers = set(present_numbers)
        intersection = winning_numbers.intersection(present_numbers)
        if len(intersection) > 0:
            points = 2 ** (len(intersection) - 1) 
            sum_points += points
    return sum_points

ans_part1 = part1(data)
print(f"Part 1 answer: {ans_part1}")


# Part 2

def part2(data):
    init_cards = len(data)
    dct_total_cards = {x: 1 for x in range(1, init_cards + 1)}  
    for idx, line in enumerate(data):
        idx += 1
        line = line.split(":")[1].strip()
        winning_numbers, present_numbers = line.split("|")
        winning_numbers = [int(x.replace(" ", "")) for x in winning_numbers.strip().split(" ") if x.isnumeric()]
        present_numbers = [int(x.replace(" ", "")) for x in present_numbers.strip().split(" ") if x.isnumeric()]
        winning_numbers = set(winning_numbers)
        present_numbers = set(present_numbers)
        wins = len(winning_numbers.intersection(present_numbers))
        for i in range(idx + 1, idx + 1 + wins):
            if i > init_cards:
                break
            dct_total_cards[i] += dct_total_cards[idx]
    total_sum = sum(dct_total_cards.values())
    return total_sum

ans_part2 = part2(data)
print(f"Part 2 answer: {ans_part2}")

