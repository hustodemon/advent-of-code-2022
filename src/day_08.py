#!/usr/bin/env python3
#
# Day 8
#
# Lessons learned:
# - uff, patience?
#

from utils import print_result, read_lines
from itertools import product


print("> Day 8")


#
# Part 1
#

lines_test = read_lines("data/day_08_test.txt")
lines = read_lines("data/day_08.txt")


def is_tree_visible(trees, x, y):
    if x in (0, len(trees[0]) - 1) or y in (0, len(trees) - 1):
        return True

    hidden_on_x1 = next((True for nx in range(x) if trees[y][nx] >= trees[y][x]), None)
    hidden_on_x2 = next((True for nx in range(x + 1, len(trees[0])) if trees[y][nx] >= trees[y][x]), None)
    hidden_on_y1 = next((True for ny in range(y) if trees[ny][x] >= trees[y][x]), None)
    hidden_on_y2 = next((True for ny in range(y + 1, len(trees[0])) if trees[ny][x] >= trees[y][x]), None)

    hidden = hidden_on_x1 and hidden_on_x2 and hidden_on_y1 and hidden_on_y2

    return not hidden


def part_1(trees):
    return len([(x, y)
                for x in range(len(trees[0])) for y in range(len(trees))
                if is_tree_visible(trees, x, y)])


print_result(1, part_1(lines_test), True)
print_result(1, part_1(lines))


#
# Part 2
#
def trees_in_scenic_view(trees, ref, coords_to_explore, acc=0):
    """
    Returns number compliant to the scenic view on given coords until first tree
    breaks scenic view (or edge is hit).
    """
    fst_coord = next(coords_to_explore, None)
    if not fst_coord:
        return acc
    elif int(trees[fst_coord[1]][fst_coord[0]]) >= ref:
        return acc + 1;
    else:
        # coords_to_explore already shorter b/c of next()
        return eat(trees, ref, coords_to_explore, acc + 1)


def scenic_score(trees, x, y):
    """Compute scenic score for tree on given coords."""
    right = trees_in_scenic_view(trees, int(trees[y][x]), ([cx, y] for cx in range(x + 1, len(trees[0]))))
    left = trees_in_scenic_view(trees, int(trees[y][x]), ([cx, y] for cx in range(x - 1, -1, -1)))
    down = trees_in_scenic_view(trees, int(trees[y][x]), ([x, cy] for cy in range(y + 1, len(trees))))
    up = trees_in_scenic_view(trees, int(trees[y][x]), ([x, cy] for cy in range(y - 1, -1, -1)))

    return right * left * down * up


def part_2(trees):
    return max(eat_all_dirs(trees, x, y)
        for x in range(0, len(trees[0]))
        for y in range(0, len(trees)))


print_result(2, part_2(lines_test), True)
print_result(2, part_2(lines))


#
# People's solution
#
