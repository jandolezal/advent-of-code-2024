"""
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5
"""

from collections import defaultdict


def prepare_input(filepath):
    protorules, protoupdates = open(filepath).read().split("\n\n")

    rules = [line.split("|") for line in protorules.strip().split("\n")]
    pages = sorted(list(set([item for row in rules for item in row])))
    updates = [line.split(",") for line in protoupdates.strip().split("\n")]

    return dict(rules=rules, updates=updates, pages=pages)


def part1(input):
    # map from page to pages (in a set) which are higher in this world
    rules = defaultdict(set)
    for f, s in input["rules"]:
        rules[f].add(s)

    updates = list(input["updates"])

    result = 0

    for update_ in updates:
        update_copy = update_[:]
        for walk in range(len(update_copy)):
            # compare neighbouring pages and if first is higher move to right
            for i in range(len(update_copy) - 1):
                f = update_copy[i]
                s = update_copy[i + 1]
                if s not in rules[f]:  # first page is higher then the second
                    page = update_copy.pop(i)
                    update_copy.insert(i + 1, page)

        if update_ == update_copy:
            result += int(update_[len(update_) // 2])

    return result


def part2(input):
    # map from page to pages (in a set) which are higher in this world
    rules = defaultdict(set)
    for f, s in input["rules"]:
        rules[f].add(s)

    updates = list(input["updates"])

    result = 0

    for update_ in updates:
        update_copy = update_[:]
        for walk in range(len(update_copy)):
            # compare neighbouring pages and if first is higher move to right
            for i in range(len(update_copy) - 1):
                f = update_copy[i]
                s = update_copy[i + 1]
                if s not in rules[f]:  # first page is higher then the second
                    page = update_copy.pop(i)
                    update_copy.insert(i + 1, page)

        # only this part differs from part 1 but i am too lazy to refactor it :-)
        if update_ != update_copy:
            result += int(update_copy[len(update_copy) // 2])

    return result


# part 1
test_input = prepare_input("05/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 143, f"Test result for part 1 should be 143, not {test_result1}"

input = prepare_input("05/input.txt")
result1 = part1(input)
print(result1)


# part 2
test_result2 = part2(test_input)
assert test_result2 == 123, f"Test result for part 2 should be 123, not {test_result2}"

result2 = part2(input)
print(result2)
