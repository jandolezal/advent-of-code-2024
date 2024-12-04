"""
--- Day 4: Ceres Search ---
https://adventofcode.com/2024/day/4
"""


def prepare_input(filepath):
    input = [list(line.strip()) for line in open(filepath).readlines()]
    return input


def part1(input, target="XMAS"):
    result = 0

    # TODO: there must be a better way:-)
    # vertical and horizontal both directions

    variants = [
        input,
        list(map(list, zip(*input))),
    ]

    for variant in variants:
        for r in range(len(variant)):
            for c in range(len(variant[0]) - len(target) + 1):  # was wrong by 1
                chars = variant[r][c : c + len(target)]
                if chars == list(target):
                    result += 1
                elif chars == list(target)[::-1]:
                    result += 1

    # diagonal
    variants = [
        input,
        [line[::-1] for line in input],
    ]

    for variant in variants:
        for r in range(len(variant[0]) - len(target) + 1):
            for c in range(len(variant) - len(target) + 1):
                chars = [variant[r + i][c + i] for i in range(len(target))]
                if chars == list(target):
                    result += 1
                elif chars == list(target)[::-1]:
                    result += 1

    return result


def part2(input):
    result = 0

    # indices of potential As in the middle of MAS or SAM
    for r in range(1, len(input) - 1):
        for c in range(1, len(input[0]) - 1):
            if input[r][c] == "A":
                # compare opposite corners
                if (
                    ((input[r - 1][c - 1] == "S") and (input[r + 1][c + 1] == "M"))
                    or ((input[r - 1][c - 1] == "M") and (input[r + 1][c + 1] == "S"))
                ) and (
                    ((input[r + 1][c - 1] == "S") and (input[r - 1][c + 1] == "M"))
                    or ((input[r + 1][c - 1] == "M") and (input[r - 1][c + 1] == "S"))
                ):
                    result += 1

    return result


# part 1
test_input = prepare_input("04/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 18, f"Test result for part 1 should be 18, not {test_result1}"

input = prepare_input("04/input.txt")
result1 = part1(input)
print(result1)

# 2469
# 2482
# 2512
# 2483
# 2556 all wrong
# 2562 is correct


# part 2
test_result2 = part2(test_input)
assert test_result2 == 9, f"Test result for part 2 should be 9, not {test_result2}"

result2 = part2(input)
print(result2)
