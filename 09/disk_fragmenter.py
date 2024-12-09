"""
--- Day 9: Disk Fragmenter ---
https://adventofcode.com/2024/day/9
"""


def prepare_input(filepath):
    return [int(num) for num in open(filepath).read().strip()]


def part1(input):
    # TODO: depending on part2 move to prepare_input
    layout = []
    for id_, blocks in enumerate(input):
        if id_ % 2 == 0:
            layout.extend([id_ // 2 for b in range(blocks)])
        else:
            layout.extend([None for b in range(blocks)])

    total = len(layout)
    # number of blocks to fill in
    free = total - sum(True for b in layout if b is not None)

    new_layout = layout[:]

    # pop from end and insert at the beginning
    for step in range(free):
        id_ = new_layout.pop(-1)
        i = new_layout.index(None)  # first None in the list
        new_layout[i] = id_

    checksum = sum(i * num for i, num in enumerate(new_layout))

    return checksum


# part 1
test_input = prepare_input("09/test_input.txt")
test_result1 = part1(test_input)
assert (
    test_result1 == 1928
), f"Test result for part 1 should be 1928 , not {test_result1}"

input = prepare_input("09/input.txt")
result1 = part1(input)
print(result1)
# 6378826667552
