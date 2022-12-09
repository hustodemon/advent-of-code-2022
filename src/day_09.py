#!/usr/bin/env python3
#
# Day 9
#
# Lessons learned:
# -
#

from utils import print_result, read_lines
from itertools import repeat, chain
from functools import reduce
from operator import add, sub
from math import dist

print("> Day 9")


#
# Part 1
#
lines_test = read_lines("data/day_09_test.txt")
lines = read_lines("data/day_09.txt")


def expand_step(step):
    """Expand step like 'R 3' into 'R' 'R' R'"""
    direction, count = step.split()
    return repeat(direction, int(count))


def expand_steps(steps):
    return chain.from_iterable(map(expand_step, steps))


dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}


def is_tail_far(head, tail):
    return max(list(map(abs, (map(sub, head, tail))))) > 1


def do_step(acc, step):
    """
    acc holds the state of the computation in a 3-tuple:
    (current head, current tail, set with tail history)
    this fn just applies the step and returns the new state
    """
    head, tail, tail_acc = acc
    new_head = tuple(map(add, head, dirs[step]))
    if is_tail_far(new_head, tail):
        tail = head
    tail_acc.add(tail)
    return (new_head, tail, tail_acc)


print_result(1, len(reduce(do_step, expand_steps(lines_test), ((0, 0), (0, 0), set()))[2]), True)
print_result(1, len(reduce(do_step, expand_steps(lines), ((0, 0), (0, 0), set()))[2]))


#
# Part 2
#
# I didn't get the problem description
#

#
# People's solution
#
