"""
--- Day 13: Claw Contraption ---
https://adventofcode.com/2024/day/13
"""

import re


def prepare_input(filepath):
    input = []
    machine_lines = open(filepath).read().split("\n\n")
    for line in machine_lines:
        numbers = [int(num) for num in re.findall(r"\d+", line)]
        input.append(
            {
                "a": (numbers[0], numbers[1]),
                "b": (numbers[2], numbers[3]),
                "prize": (numbers[4], numbers[5]),
            }
        )

    return input


def part1(input):
    machine_results = []

    for machine in input:
        x = machine["prize"][0]
        y = machine["prize"][1]

        for a in range(max(x, y)):
            try:
                b = int((y - machine["a"][1] * a) / machine["b"][1])
                temp_x = int(machine["a"][0] * a + machine["b"][0] * b)
                temp_y = int(machine["a"][1] * a + machine["b"][1] * b)
                if (temp_x == x) and (temp_y == y) and (b >= 0):
                    machine_results.append((a, b))
                    break
            except ValueError:
                continue

    return sum(a * 3 + b * 1 for a, b in machine_results)


# part 1
test_input = prepare_input("13/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 480, f"Test result for part 1 should be 480, not {test_result1}"

input = prepare_input("13/input.txt")
result1 = part1(input)
print(result1)
# 38069 is wrong
# 36870
