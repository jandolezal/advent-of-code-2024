"""
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5
"""

from collections import defaultdict


def prepare_input(filepath):
    protorules, protoupdates = open(filepath).read().split("\n\n")

    protorules = [line.split("|") for line in protorules.strip().split("\n")]

    rules = defaultdict(set)
    for f, s in protorules:
        rules[f].add(s)

    updates = [line.split(",") for line in protoupdates.strip().split("\n")]

    return dict(rules=rules, updates=updates)


def part1(input):
    rules = input["rules"]
    updates = [line[::-1] for line in input["updates"]]
    results = []
    correct_update = True

    # going backwards in original updates
    # the rules dict is using preceding page as a key
    for update in updates:
        for i in range(len(update)):
            if set(update[i:]) & rules[update[i]]:
                correct_update = False
                break
        if correct_update:
            results.append(update)
        correct_update = True

    return sum([int(item[len(item) // 2]) for item in results])


# part 1
test_input = prepare_input("05/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 143, f"Test result for part 1 should be 143, not {test_result1}"

input = prepare_input("05/input.txt")
result1 = part1(input)
print(result1)
