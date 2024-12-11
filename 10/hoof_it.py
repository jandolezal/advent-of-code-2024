"""
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10
"""



def prepare_input(filepath):
    input = {}
    lines = [list(line.strip()) for line in open(filepath).readlines()]
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            input[(r, c)] = int(lines[r][c])
    return input


def hike(step, height, input):
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # stay on map
    rows, cols = max(input.keys())[0], max(input.keys())[1]

    if height == 9:
        # gather all reached peaks even duplicate positions
        # handle later when calculating scores
        yield step
    else:
        neighbours = {}
        for offset in offsets:
            neighbour = (step[0] + offset[0], step[1] + offset[1])
            # is it on a map and higher one point?
            if (
                (neighbour[0] >= 0)
                and (neighbour[1] >= 0)
                and (neighbour[0] <= rows)
                and (neighbour[1] <= cols)
                and (input[neighbour] == height + 1)
            ):
                neighbours[neighbour] = input[neighbour]
        for neighbour, height in neighbours.items():
            yield from hike(neighbour, height, input)


def part1(input):
    trailheads = {k: v for k, v in input.items() if v == 0}

    results = {}

    for step, height in trailheads.items():
        results[step] = list(hike(step, height, input))

    # unique number of peaks per trailhead
    return sum(len(set(peaks)) for t, peaks in results.items())


def part2(input):
    trailheads = {k: v for k, v in input.items() if v == 0}

    results = {}

    for step, height in trailheads.items():
        results[step] = list(hike(step, height, input))

    # only this differs from from part1
    # unique trails to the peak per traihead
    return sum(len(peaks) for t, peaks in results.items())


# part 1
test_input = prepare_input("10/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 36, f"Test result for part 1 should be 36, not {test_result1}"

input = prepare_input("10/input.txt")
result1 = part1(input)
print(result1)
# 798


# part 2
test_result2 = part2(test_input)
assert test_result2 == 81, f"Test result for part 2 should be 81, not {test_result2}"

result2 = part2(input)
print(result2)
# 1816
