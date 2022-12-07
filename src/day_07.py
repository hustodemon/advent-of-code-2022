#!/usr/bin/env python3
#
# Day 7
#
# Lessons learned:
# -
#

from utils import print_result, read_lines
from pprint import pprint


print("> Day 7")


#
# Part 1
#

#print_result(1, "123", True)
lines_test = read_lines("data/day_07_test.txt")
lines = read_lines("data/day_07.txt")

# gotta steal this
# how t.f. doesn't have python this built-in?
def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct


def apply_instr(tree, path, inst):
    """
    Apply single instruction and mutate tree/or path based on it.
    A mutating sollution. Sorry Alonso Church.
    """
    match inst.split():
        case ['$', 'cd', '..']:
            path.pop()
        case ['$', 'cd', dir_name]:
            cur_dir = safeget(tree, *path)
            cur_dir[dir_name] = {}
            path.append(dir_name)
        case [size, fname] if size not in ("dir", "$"):
            cur_dir = safeget(tree, *path)
            cur_dir[fname] = int(size)


def populate_fs_tree(instructions):
    tree = {}
    path = []
    for i in instructions:
        apply_instr(tree, path, i)
    return tree


def df(tree, acc):
    fsizes = 0
    for fname in tree.keys():
        if isinstance(tree[fname], int):  # file
            fsizes += tree[fname]
        else:  # dir
            fsizes += df(tree[fname], acc)

    acc.append(fsizes)
    return fsizes


def compute(lines):
    """Return a tuple with the solutions (part1, part2)."""
    tree = populate_fs_tree(lines)
    acc = []
    df(tree["/"], acc)
    used = max(acc)
    return (
        sum(s for s in acc if s <= 100000),
        sorted(s for s in acc if used - s < 40000000)[0]
        )



result_test = compute(lines_test)
result = compute(lines)
print_result(1, result_test[0], True)
print_result(1, result[0])
print_result(2, result_test[1], True)
print_result(2, result[1])

#
# People's solution
#
