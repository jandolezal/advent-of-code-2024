"""
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2
"""


def prepare_input(filepath):
    input = [[int(num) for num in row.split()] for row in open(filepath).readlines()]
    return input


def descending(row):
    return all(row[i] > row[i + 1] for i in range(len(row) - 1))


def ascending(row):
    return all(row[i] < row[i + 1] for i in range(len(row) - 1))


def within_limit(row):
    return all(abs(row[i] - row[i + 1]) in [1, 2, 3] for i in range(len(row) - 1))


def part1(input):
    result = 0

    for row in input:
        if (descending(row) or ascending(row)) and within_limit(row):
            result += 1

    return result


def part2(input):
    result = 0

    for row in input:
        if (descending(row) or ascending(row)) and within_limit(row):
            result += 1
        else:
            for i in range(len(row)):
                alt_row = row[:]
                alt_row.pop(i)
                if (descending(alt_row) or ascending(alt_row)) and within_limit(alt_row):
                    result += 1
                    break

    return result


# part 1
test_input = prepare_input("02/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 2, f"Test result for part 1 should be 2, not {test_result1}"

input = prepare_input("02/input.txt")
result1 = part1(input)
print(result1)


# part 2
test_result2 = part2(test_input)
assert test_result2 == 4, f"Test result for part 2 should be 4, not {test_result2}"

result2 = part2(input)
print(result2)
