"""
https://adventofcode.com/2025/day/4

--- Day 4: Printing Department ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the banks text file")

parser.add_argument("--file", type=str, help="input.txt for the day 4 of advent of code")

args = parser.parse_args()

grids = []

with open(args.file, 'r') as file:
    for line in file:
        rows = list(line.strip())
        grids.append(rows)

rows = len(grids[0])
cols = len(grids)

def check_paper_roll(grids, row, col):
    if grids[row][col] == '@':
        return True
    return False

def check_neighbor(grids, row, col, paper_count):

    max_row = len(grids)
    max_col = len(grids[0])

    # 1. Check Top-Left (row-1, col-1)
    if (row - 1) >= 0 and (col - 1) >= 0:
        if check_paper_roll(grids, row - 1, col - 1):
            paper_count += 1
    
    # 2. Check Top (row-1, col)
    if (row - 1) >= 0:
        if check_paper_roll(grids, row - 1, col):
            paper_count += 1

    # 3. Check Top-Right (row-1, col+1)
    if (row - 1) >= 0 and (col + 1) < max_col:
        if check_paper_roll(grids, row - 1, col + 1):
            paper_count += 1

    # 4. Check Left (row, col-1)
    if (col - 1) >= 0:
        if check_paper_roll(grids, row, col - 1):
            paper_count += 1
    
    # 5. Check Right (row, col+1)
    if (col + 1) < max_col:
        if check_paper_roll(grids, row, col + 1):
            paper_count += 1
    
    # 6. Check Bottom-Left (row+1, col-1)
    if (row + 1) < max_row and (col - 1) >= 0:
        if check_paper_roll(grids, row + 1, col - 1):
            paper_count += 1
    
    # 7. Check Bottom (row+1, col)
    if (row + 1) < max_row:
        if check_paper_roll(grids, row + 1, col):
            paper_count += 1
    
    # 8. Check Bottom-Right (row+1, col+1)
    if (row + 1) < max_row and (col + 1) < max_col:
        if check_paper_roll(grids, row + 1, col + 1):
            paper_count += 1

    if paper_count < 4:
        return True, paper_count
    else:
        return False, paper_count


accessible = 0

for row in range(rows):
    for col in range(cols):
        paper_count = 0
        if grids[row][col] == '.': continue
            
        isValid, paper_count = check_neighbor(grids, row, col, paper_count)
        
        if isValid:
            accessible += 1


print("Accessible Rolls: ", accessible)
            