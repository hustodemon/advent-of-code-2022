#!/usr/bin/env python3
#
# Day 14
#
# Lessons learned:
# -
#

from utils import print_result, read_lines
from functools import reduce
from itertools import dropwhile


print("> Day 14")


lines_test = read_lines("../data/day_14_test.txt")
lines = read_lines("../data/day_14.txt")


def path_points(start, end):
    step_x = 1 if start[0] < end[0] else -1
    step_y = 1 if start[1] < end[1] else -1
    return [(x, y)
            for x in range(start[0], end[0] + step_x, step_x)
            for y in range(start[1], end[1] + step_y, step_y)]


def add_path_to_set(path, s):
    if len(path) > 1:
        p1, p2, *rst = path
        s.update(path_points(p1, p2))
        add_path_to_set(path[1:], s)


def parse_tuple(s):
    return tuple(map(int, s.split(",")))


def parse_lines(lines):
    return [list(map(parse_tuple, path.split(" -> "))) for path in lines]


def safenext(it, default=None):
    try:
        return next(it)
    except StopIteration:
        return default


def drop(sand_pos, obstacles, floor_y = None):
    """
    Move the sand_pos lower, if possible.
    If not possible (no feasible position or floor hit), return None.
    """
    if floor_y and sand_pos[1] + 1 >= floor_y:
        return None

    new_pos = dropwhile(
        lambda pos: pos in obstacles,
        (
            (sand_pos[0], sand_pos[1] + 1),
            (sand_pos[0] - 1, sand_pos[1] + 1),
            (sand_pos[0] + 1, sand_pos[1] + 1),
        )
    )

    return safenext(new_pos)


def compute(lines, use_floor=False):
    obstacles = set()
    for path in parse_lines(lines):
        add_path_to_set(path, obstacles)
    rock_count = len(obstacles)
    last_rock_y = max(rock[1] for rock in obstacles)
    end_point_y = last_rock_y + 2 if use_floor else last_rock_y

    sand = (500, 0)
    while sand[1] <= end_point_y:
        new_sand = drop(sand, obstacles, end_point_y if use_floor else None)
        if new_sand:
            sand = new_sand
        else:
            obstacles.add(sand)
            if sand == (500, 0):
                break
            sand = (500, 0)

    return len(obstacles) - rock_count

print_result(1, compute(lines_test), True)
print_result(1, compute(lines), True)

print_result(2, compute(lines_test, True))
print_result(2, compute(lines, True))

#
# People's solution
#
