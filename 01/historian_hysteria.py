"""
--- Day 1: Historian Hysteria ---
https://adventofcode.com/2024/day/1
"""


def prepare_input(filepath):
    raw_input = []
    for row in open(filepath).readlines():
        raw_input.append([int(num) for num in row.split()])
    return [list(col) for col in list(zip(*raw_input))]


def part1(input):
    group1 = sorted(input[0])
    group2 = sorted(input[1])

    result = sum([abs(first - second) for first, second in zip(group1, group2)])

    return result


def part2(input):
    result = 0
    for num in input[0]:
        result += num * input[1].count(num)
    return result


# part 1
test_input = prepare_input("01/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 11, f"Test result for part 1 should be 11, not {test_result1}"

input = prepare_input("01/input.txt")
result1 = part1(input)
print(result1)

# part 2
test_result2 = part2(test_input)
assert test_result2 == 31, f"Test result for part 2 should be 31, not {test_result2}"
result2 = part2(input)
print(result2)
