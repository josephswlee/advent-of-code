"""
https://adventofcode.com/2025/day/5

--- Day 5: Cafeteria ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the banks text file")

parser.add_argument("--file", type=str, help="input.txt for the day 5 of advent of code")

args = parser.parse_args()

ingredient_ranges = []
with open(args.file, 'r') as file:
    for line in file:
        ingredient_ranges.extend(line.split())

id_ranges = []
ingredient_ids = []
for i in range(len(ingredient_ranges)):
    if '-' in ingredient_ranges[i]:
        id_ranges.append(ingredient_ranges[i])
    else:
        ingredient_ids.append(ingredient_ranges[i])

# Part 1 Answer

fresh_num = 0

for ingredient_id in ingredient_ids:

    for id_range in id_ranges:
        begining_num, ending_num = id_range.split('-')
        
        if int(begining_num) <= int(ingredient_id) <= int(ending_num):
            fresh_num += 1
            break
        else: continue

print('fresh_num: ', fresh_num)

# Part 2 Answer

fresh_id_count = 0
list_ranges = []
for id_range in id_ranges:
    begining_num, ending_num = id_range.split('-')
    begining_num, ending_num = int(begining_num), int(ending_num)
    list_ranges.append([begining_num, ending_num])

# Sort by the beginning number
list_ranges.sort(key=lambda x: x[0])

merged_ranges = []

for curr_start, curr_end in list_ranges:
    # initially if merged_ranges is empty
    if not merged_ranges:
        merged_ranges.append([curr_start, curr_end])

    else:
        # get the last range from the merged ranges
        last_range = merged_ranges[-1]
        last_start, last_end = last_range[0], last_range[1]

        # if current start is less or equal to last end
        # this means there is overlap (since the ranges are sorted)
        # e.g., given curr [10,14] and last [3,5] there is no overlap
        # if curr_start (10) is not <= last_end (5)
        if curr_start <= last_end:
            # as there is an overlap find the max of the curr end and last end
            merged_ranges[-1][1] = max(curr_end, last_end)

        # since there is no overlap append
        else:
            merged_ranges.append([curr_start, curr_end])

total_count = 0

for merged in merged_ranges:
    temp = merged[1] - merged[0] + 1
    total_count += temp

print(total_count)
    