"""
https://adventofcode.com/2025/day/2

--- Day 2: Gift Shop ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the password text file")

parser.add_argument("--file", type=str, help="input.txt for the day 2 of advent of code")

args = parser.parse_args()

ids = []

with open(args.file, 'r') as file:
    for line in file:
        clean_line = line.strip().split(',')
        ids.extend(clean_line)

def check_substring(id):
    """
    Condition is to make sure that output is even and repeated twice
    
    This logic is able to check even number and only repeat twice

    original logic :
    s = str(id)
    ss = s[1:] + s[:-1]
    return s in ss 
    """
    id = str(id)
    n = len(id)
    if n % 2 != 0:
        return False

    mid = n // 2

    return id[:mid] == id[mid:]


invalid_ids = []

for id_range in ids:
    
    start_id, end_id = id_range.split('-')[0], id_range.split('-')[1]
    
    start_id = int(start_id)
    end_id = int(end_id)

    while start_id <= end_id:

        if check_substring(start_id):
            invalid_ids.append(start_id)
        start_id += 1

ans = 0

for i in invalid_ids:
    ans += i

print(ans)
