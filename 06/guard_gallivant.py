"""
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/6
"""

from collections import namedtuple

Point = namedtuple("Point", ["r", "c"])


class Lab:
    def __init__(self, length, width, obstructions):
        self.length = length
        self.width = width
        self.obstructions = obstructions

    def __repr__(self):
        return repr(f"Lab(length={self.length},width={self.width})")


class Guard:
    def __init__(self, position, orientation, route=None):
        self.position = position
        self.orientation = orientation
        if not route:
            self.route = []

    def walk(self, lab):
        if self.orientation == "N":
            target = Point(self.position.r - 1, self.position.c)
        elif self.orientation == "E":
            target = Point(self.position.r, self.position.c + 1)
        elif self.orientation == "S":
            target = Point(self.position.r + 1, self.position.c)
        elif self.orientation == "W":
            target = Point(self.position.r, self.position.c - 1)

        direction_change = {"N": "E", "E": "S", "S": "W", "W": "N"}

        if (
            (target.r < 0)
            or (target.c < 0)
            or (target.r > lab.length)
            or (target.c > lab.width)
        ):
            return False
        if target in lab.obstructions:
            self.orientation = direction_change[self.orientation]
            return True
        else:
            self.position = target
            self.route.append(target)
            return True

    def calculate_route(self):
        return len(set([(field.r, field.c) for field in self.route]))

    def __repr__(self):
        return repr(
            f"Guard(position=Point({self.position.r},{self.position.c}), orientation='{self.orientation}')"
        )


def prepare_input(filepath):
    input = [list(line.strip()) for line in open(filepath).readlines()]

    obstructions = []

    directions = {"^": "N", ">": "E", "v": "S", "<": "W"}

    for r in range(len(input)):
        for c in range(len(input[0])):
            symbol = input[r][c]
            if symbol == "#":
                obstructions.append(Point(r, c))
            elif symbol in directions.keys():
                guard = Guard(position=Point(r, c), orientation=directions[symbol])

    lab = Lab(length=len(input), width=len(input[0]), obstructions=obstructions)

    return dict(guard=guard, lab=lab)


def part1(input):
    guard = input["guard"]
    lab = input["lab"]

    ok_to_go = True

    while ok_to_go:
        ok_to_go = guard.walk(lab)
    return guard.calculate_route() - 1  # without starting field


# part 1
test_input = prepare_input("06/test_input.txt")
test_result1 = part1(test_input)
assert test_result1 == 41, f"Test result for part 1 should be 41, not {test_result1}"

input = prepare_input("06/input.txt")
result1 = part1(input)
print(result1)
