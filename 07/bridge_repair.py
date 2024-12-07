"""
--- Day 7: Bridge Repair ---
https://adventofcode.com/2024/day/7
"""

# TODO: Reimplement to account for duplicate totals in final input data

import operator


def prepare_input(filepath):
    input = {}
    for line in open(filepath).readlines():
        input[int(line.split(":")[0])] = [
            int(num) for num in line.strip("\n").split(":")[1].split(" ") if num
        ]
    return input


def calibrate(total, subtotal, numbers):
    if not numbers:
        yield subtotal
    else:
        for o in (operator.add, operator.mul):
            yield from calibrate(total, o(subtotal, numbers[0]), numbers[1:])


def part1(input):
    result = {}
    for total, numbers in input.items():
        result[total] = list(calibrate(total, numbers[0], numbers[1:]))
    calculated_result = sum(
        {total: subtotals for total, subtotals in result.items() if total in subtotals}
    )
    return calculated_result


# part 1
test_input = prepare_input("07/test_input.txt")
test_result1 = part1(test_input)
assert (
    test_result1 == 3749
), f"Test result for part 1 should be 3749 , not {test_result1}"

input = prepare_input("07/input.txt")
result1 = part1(input)
print(result1)
# 3312272361386 is wrong

# Current implementation does not expect duplicate keys in input data. Fixing manually for now...
# 850 rows but 849 unique totals
# 864: 9 62 7 8 772 6
# 864: 1 3 3 16 9

# 3312271364788 + 864 = 3312271365652 is correct


def calibrate(total, subtotal, numbers):
    if not numbers:
        yield subtotal
    else:
        for o in (operator.add, operator.mul, lambda f, s: int(str(f) + str(s))):
            yield from calibrate(total, o(subtotal, numbers[0]), numbers[1:])


def part2(input):
    result = {}
    for total, numbers in input.items():
        result[total] = list(calibrate(total, numbers[0], numbers[1:]))
    calculated_result = sum(
        {total: subtotals for total, subtotals in result.items() if total in subtotals}
    )
    return calculated_result


# part 2
test_result2 = part2(test_input)
assert (
    test_result2 == 11387
), f"Test result for part 2 should be 11387, not {test_result2}"

result2 = part2(input)
print(result2)

# 509463489295848 + 864 = 509463489296712
