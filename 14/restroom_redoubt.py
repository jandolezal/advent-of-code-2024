"""
--- Day 14: Restroom Redoubt ---
https://adventofcode.com/2024/day/14

"""

from collections import defaultdict
from dataclasses import dataclass
import math
import re


@dataclass
class Robot:
    x: int
    y: int
    right: int
    down: int


def prepare_input(filepath):
    numbers = [
        re.findall(r"-{0,1}\d+", row.strip()) for row in open(filepath).readlines()
    ]
    input = [Robot(*[int(num) for num in nums]) for nums in numbers]
    return input


def _calculate_quadrants_counts(robots, width, length):
    quadrants = defaultdict(int)
    horizontal = width // 2
    vertical = length // 2

    for robot in robots:
        if (robot.x < horizontal) and (robot.y < vertical):
            quadrants["top_left"] += 1
        elif (robot.x < horizontal) and (robot.y > vertical):
            quadrants["bottom_left"] += 1
        elif (robot.x > horizontal) and (robot.y < vertical):
            quadrants["top_right"] += 1
        elif (robot.x > horizontal) and (robot.y > vertical):
            quadrants["bottom_right"] += 1
    return quadrants


def part1(input, width, length, steps=100):
    robots = []
    for step in range(steps):
        for robot in input:  # [10:11]
            x = robot.x + robot.right
            y = robot.y + robot.down
            if x < 0:
                robot.x = width + x
            elif x >= width:
                robot.x = x - width
            else:
                robot.x = x
            if y < 0:
                robot.y = length + y
            elif y >= length:
                robot.y = y - length
            else:
                robot.y = y
            # print(step, robot)
            if step == steps - 1:
                robots.append(robot)

    results = _calculate_quadrants_counts(robots, width, length)
    return math.prod(v for v in results.values())


# part 1
test_input = prepare_input("14/test_input.txt")
test_result1 = part1(test_input, 11, 7)
assert test_result1 == 12, f"Test result for part 1 should be 12, not {test_result1}"

input = prepare_input("14/input.txt")
result1 = part1(input, 101, 103)
print(result1)
# 220971520
