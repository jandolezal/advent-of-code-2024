"""
--- Day 9: Disk Fragmenter ---
https://adventofcode.com/2024/day/9
"""

from collections import defaultdict


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


def _calculate_free_spaces(layout):
    """Create map from index in layout to number of free blocks since index."""
    free_streak = False
    free_spaces = defaultdict(int)

    for i, item in enumerate(layout):
        if item is None and not free_streak:  # new free space
            free_i = i
            free_spaces[free_i] += 1
            free_streak = True
        elif item is None and free_streak:  # continuing in free space
            free_spaces[free_i] += 1
        else:  # must be file block
            free_streak = False

    return free_spaces


def part2(input):
    # TODO: depending on part2 move to prepare_input
    layout = []
    for id_, blocks in enumerate(input):
        if id_ % 2 == 0:
            layout.extend([id_ // 2 for b in range(blocks)])
        else:
            layout.extend([None for b in range(blocks)])

    size = len(layout)
    max_id_ = id_ // 2
    # this will be updated
    new_layout = layout[:]
    # this stays the same
    # used to calculate indexes of id_ which we do only once per id_
    new_layout_reversed = new_layout[::-1]

    free_spaces = _calculate_free_spaces(new_layout)

    for id_ in range(max_id_, 0, -1):  # descending from highest id_
        # logic for removing blocks
        start = new_layout.index(id_)
        end = size - new_layout_reversed.index(id_)
        blocks_to_move = end - start

        try:
            # logic for inserting blocks
            # find suitable free space
            for i, spots in free_spaces.items():
                if (spots >= blocks_to_move) and (i <= start):
                    new_layout[start:end] = [None] * blocks_to_move
                    new_layout[i : i + blocks_to_move] = [id_] * blocks_to_move
                    free_spaces = _calculate_free_spaces(new_layout)
                    break
        except ValueError:
            continue

    checksum = sum(i * num for i, num in enumerate(new_layout) if num is not None)

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


# part 2
test_result2 = part2(test_input)
assert (
    test_result2 == 2858
), f"Test result for part 2 should be 2858, not {test_result2}"

result2 = part2(input)
print(result2)
# 6413328569890
