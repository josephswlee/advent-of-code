"""
https://adventofcode.com/2025/day/7

--- Day 7: Laboratories ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the banks text file")

parser.add_argument("--file", type=str, help="input.txt for the day 7 of advent of code")

args = parser.parse_args()

grids = []

with open(args.file, 'r') as file:

    for line in file:
        grids.append(list(line.strip()))

rows = len(grids)
cols = len(grids[0])

total_count = 0

for row in range(len(grids)):
    for col in range(len(grids[0])):

        if grids[row][col] == 'S':
            print("true")
            if grids[row+1][col] == '.':
                grids[row+1][col] = '|'
        
        elif grids[row][col] == '^':
            if grids[row][col-1] == '.':
                grids[row][col-1] = '|'
                
            if grids[row][col+1] == '.':
                grids[row][col+1] = '|'
                
        else:
            if grids[row-1][col]:
                if grids[row-1][col] == '|':
                    grids[row][col] = '|'
                    
# Visualize
# for row in grids:
#     print("".join(row))

for row in range(len(grids)):
    for col in range(len(grids[0])):

        if grids[row][col] == '^':
            if grids[row-1][col] == '|':
                total_count += 1

print(total_count)
