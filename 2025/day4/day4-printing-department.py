"""
https://adventofcode.com/2025/day/4

--- Day 4: Printing Department ---
"""

import argparse

parser = argparse.ArgumentParser(description="Pass in the banks text file")

parser.add_argument("--file", type=str, help="input.txt for the day 4 of advent of code")

args = parser.parse_args()

