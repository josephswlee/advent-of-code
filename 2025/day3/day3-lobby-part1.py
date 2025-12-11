"""
https://adventofcode.com/2025/day/3

--- Day 3: Lobby ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the password text file")

parser.add_argument("--file", type=str, help="input.txt for the day 2 of advent of code")

args = parser.parse_args()

banks = []
with open(args.file, 'r') as file:
    for line in file:
        banks.append(line.strip())

joltages = []

for bank in banks:
    left, right = 0, 0
    highest = 0
    
    for left in range(len(bank)):
        right = left + 1
        if left == right: break
        while right < len(bank):
            
            highest = max(highest, int(bank[left]+bank[right]))
            right += 1

    joltages.append(highest)

answer = 0
for joltage in joltages:
    answer += joltage

print(joltages)
print(answer)
