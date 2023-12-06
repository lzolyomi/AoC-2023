import re
from tqdm import tqdm

DAY = 5

# Parse data
with open(f"data/day{DAY}.txt", "r") as f:
    data = f.read().splitlines()
    seeds = [int(x.strip()) for x in data[0].split(":")[1].strip().split(" ")]
    map_pattern = r"(\w+)-to-(\w+) map"
    range_pattern = r"(\d+) (\d+) (\d+)"
    maps = {}
    for line in data[1:]:
        m = re.match(map_pattern, line)
        if m:
            src, dest = m.groups()
            assert f"{src}-{dest}" not in maps, f"Duplicate map: {src}-{dest}"
            maps[f"{src}-{dest}"] = []
        elif re.match(range_pattern, line):
            m_range = re.match(range_pattern, line)
            dst_start, src_start, length = m_range.groups()
            maps[f"{src}-{dest}"].append((range(int(src_start), int(src_start) + int(length)), range(int(dst_start), int(dst_start) + int(length))))

# Part 1

def part1():
    mapping_order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    map_keys_ordered = [f"{mapping_order[i-1]}-{mapping_order[i]}" for i in range(1, len(mapping_order))]
    global seeds, maps
    locations = []
    for seed in seeds:
        for map_key in map_keys_ordered:
            for src_range, dst_range in maps[map_key]:
                if seed in src_range:
                    seed = dst_range.start + seed - src_range.start
                    break
        locations.append(seed) 
    return min(locations)

print(f"Part 1: {part1()}")

# Part 2
seed_ranges = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds)-1,2)]

def part2(seeds, maps):
    mapping_order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    map_keys_ordered = [f"{mapping_order[i-1]}-{mapping_order[i]}" for i in range(1, len(mapping_order))]

    res = 2**64
    for seed_start, offset in zip(seeds[::2], seeds[1::2]):
        ranges = [(seed_start, seed_start + offset - 1)]
        for map_key in map_keys_ordered:
            new_ranges = []
            for low, high in ranges:
                found = False
                for src_range, dest_range in maps[map_key]:
                    src_start, src_end = src_range.start, src_range.stop - 1
                    dest_start = dest_range.start
                    if low >= src_start and high <= src_end:
                        new_ranges.append((low - src_start + dest_start, high - src_start + dest_start))
                        found = True
                    elif low < src_start <= high <= src_end:
                        ranges.append((low, src_start - 1))
                        new_ranges.append((dest_start, dest_start + high - src_start))
                        found = True
                    elif src_start <= low <= src_end < high:
                        ranges.append((src_end + 1, high))
                        new_ranges.append((dest_start + low - src_start, dest_start + src_end - src_start))
                        found = True
                    elif low < src_start and high > src_end:
                        ranges.append((low, src_start - 1))
                        ranges.append((src_end + 1, high))
                        new_ranges.append((dest_start, dest_start + src_end - src_start))
                        found = True
                    if found:
                        break
                if not found:
                    new_ranges.append((low, high))
            ranges = new_ranges.copy()
        res = min(res, min(ranges, key=lambda x: x[0])[0])
    return res

# Assuming 'seeds' and 'maps' are already defined as per your parsing logic
print(f"Part 2: {part2(seeds, maps)}")
