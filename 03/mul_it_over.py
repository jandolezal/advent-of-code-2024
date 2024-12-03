"""
--- Day 3: Mull It Over ---
https://adventofcode.com/2024/day/3
"""

import re


def prepare_input(filepath):
    input = open(filepath).read()
    return input


def part1(input):
    pattern = r"mul\(\d+,\d+\)"  # mul(11,8)
    subpattern = r"\d+,\d+"  # 11,8

    occurences = re.findall(pattern, input)
    numbers = [
        [int(num) for num in re.search(subpattern, item).group(0).split(",")]
        for item in occurences
    ]
    multiplications = [first * second for first, second in numbers]

    return sum(multiplications)


def part2(input):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    subpattern = r"\d+,\d+"
    enabled = True

    occurences = re.findall(pattern, input)
    result = 0
    for item in occurences:
        if item == "don't()":
            enabled = False
        elif item == "do()":
            enabled = True
        else:
            numbers = [
                int(num) for num in re.search(subpattern, item).group(0).split(",")
            ]
            if enabled:
                result += numbers[0] * numbers[1]

    return result


# part 1
test_input = prepare_input("03/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 161, f"Test result for part 1 should be 161, not {test_result1}"

input = prepare_input("03/input.txt")
result1 = part1(input)
print(result1)


# part 2
test_result2 = part2(test_input)
assert test_result2 == 48, f"Test result for part 2 should be 48, not {test_result2}"

result2 = part2(input)
print(result2)
