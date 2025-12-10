"""
https://adventofcode.com/2025/day/1

--- Day 1: Secret Entrance ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the password text file")

parser.add_argument("--file", type=str, help="password.txt for the day 1 of advent of code")

args = parser.parse_args()

lines = []

with open(args.file, "r") as file:
    for line in file:
        stripped_line = line.strip()
        lines.append(stripped_line)

dial = 50

n = 100

passcode = 0

output = []

def normalize(num):
    if num <0:
        num = 100 + num

    elif num > 99:
        num = num - 100

    return num

for i in range(len(lines)):
    direction, num = lines[i][0], lines[i][1:]
    num = int(num)

    if direction == 'L':
        dial -= num

        while dial < 0 or dial > 99:
            dial = normalize(dial)

        if dial == 100:
            dial = 0

        if dial == 0:
            passcode += 1
    
    else:
        dial += num

        while dial < 0 or dial > 99:
            dial = normalize(dial)

        if dial == 100:
            dial = 0

        if dial == 0:
            passcode += 1

    output.append(dial)

"""
Debug code 

file_path = "day1-debug-output.txt"

with open(file_path, 'w') as file:
    lines_with_newlines = (str(item) + '\n' for item in output)
    file.writelines(lines_with_newlines)

    print(f"Successfully wrote list to {file_path}")

print(passcode)

"""
