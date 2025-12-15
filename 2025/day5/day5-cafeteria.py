"""
https://adventofcode.com/2025/day/5

--- Day 5: Cafeteria ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the banks text file")

parser.add_argument("--file", type=str, help="input.txt for the day 4 of advent of code")

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

fresh_num = 0

for ingredient_id in ingredient_ids:

    for id_range in id_ranges:
        begining_num, ending_num = id_range.split('-')
        
        if int(begining_num) <= int(ingredient_id) <= int(ending_num):
            fresh_num += 1
            break
        else: continue

print('fresh_num: ', fresh_num)

        