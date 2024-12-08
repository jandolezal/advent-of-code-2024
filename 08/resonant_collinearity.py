"""
--- Day 8: Resonant Collinearity ---
https://adventofcode.com/2024/day/8
"""

from collections import defaultdict
from itertools import combinations


def prepare_input(filepath):
    input = defaultdict(list)

    lines = [line.strip() for line in open(filepath).readlines()]

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != ".":
                input[lines[r][c]].append((r, c))

    return dict(coordinates=input, lines=lines)


def part1(input):
    coordinates = input["coordinates"]
    # just to know the grid boundaries
    lines = input["lines"]

    # for each frequency relevant antinodes
    antinodes = defaultdict(list)

    for frequency, coors in coordinates.items():
        pairs = list(combinations(coors, 2))
        for f, s in pairs:
            diff = s[0] - f[0], s[1] - f[1]
            candidate1 = (f[0] - diff[0], f[1] - diff[1])
            candidate2 = (s[0] + diff[0], s[1] + diff[1])
            for candidate in [candidate1, candidate2]:
                # check if the candidate coordinates are out of the grid
                if (
                    (candidate[0] >= 0)
                    and (candidate[1] >= 0)
                    and (candidate[0] < len(lines))
                    and (candidate[1] < len(lines[0]))
                ):
                    antinodes[frequency].append(candidate)

    return len(
        set([item for sublist in antinodes.values() for item in sublist])
    )  # unique antinodes


# part 1
test_input = prepare_input("08/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 14, f"Test result for part 1 should be 14 , not {test_result1}"

input = prepare_input("08/input.txt")
result1 = part1(input)
print(result1)
# 354 is correct