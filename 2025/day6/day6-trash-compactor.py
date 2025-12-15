"""
https://adventofcode.com/2025/day/6

--- Day 6: Trash Compactor ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the banks text file")

parser.add_argument("--file", type=str, help="input.txt for the day 4 of advent of code")

args = parser.parse_args()

math_problems = []

with open(args.file, 'r') as file:
    for line in file:
        math_problems.append(line.strip().split(' '))

# clean up empty space in place
for math_problem in math_problems:
    math_problem[:] = [item for item in math_problem if item != '']

import numpy as np

math_problems_array = np.array(math_problems)
transposed_math_problems = math_problems_array.T.tolist()

answers = []

for problem in transposed_math_problems:
    operator = problem[-1]
    
    if operator == "*":
        calc_val = 1
        for num in problem[:-1]:
            calc_val *= int(num)
        answers.append(calc_val)
    else:
        calc_val = 0
        for num in problem[:-1]:
            calc_val += int(num)
        answers.append(calc_val)

result = 0

for answer in answers:
    result += answer

print(result)
