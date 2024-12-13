"""
--- Day 11: Plutonian Pebbles ---
https://adventofcode.com/2024/day/11
"""

from collections import defaultdict


def prepare_input(filepath):
    return [int(item) for item in open(filepath).read().strip().split(" ")]


def part1(input, blinks=25):
    stones = input[:]
    new_stones = []

    for blink in range(blinks):
        print(blink, len(stones))
        for stone in stones:
            num_digits = len(str(stone))
            if stone == 0:
                new_stones.append(1)
            elif num_digits % 2 == 0:
                first = int(str(stone)[: num_digits // 2])
                second = int(str(stone)[num_digits // 2 :])
                new_stones.extend([first, second])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones[:]
        new_stones = []

    return len(stones)


def part2(input, blinks=25):
    stones = {stone: 1 for stone in input}

    for blink in range(blinks):
        # print(blink, len(stones))
        new_stones = defaultdict(int)

        for stone, count in stones.items():
            num_digits = len(str(stone))
            if stone == 0:
                new_stones[1] += count
            elif num_digits % 2 == 0:
                first = int(str(stone)[: num_digits // 2])
                second = int(str(stone)[num_digits // 2 :])
                new_stones[first] += count
                new_stones[second] += count
            else:
                new_stones[stone * 2024] += count

        stones = new_stones

    return sum(count for count in stones.values())


# part 1
test_input = prepare_input("11/test_input.txt")
test_result1 = part1(test_input)
assert (
    test_result1 == 55312
), f"Test result for part 1 should be 55312, not {test_result1}"

input = prepare_input("11/input.txt")
result1 = part1(input)
print(result1)
# 198089


# part 2
test_result2 = part2(test_input)
assert (
    test_result2 == 55312
), f"Test result for part 2 should be 55312, not {test_result2}"

result2 = part2(input, blinks=75)
print(result2)
# 236302670835517
