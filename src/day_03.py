#!/usr/bin/env python3
#
# Day 3
#
# Lessons learned:
# - division: /, whole number division: //
# - list split: [:2], [2:], [-1:], [:-1]
# - set: adding with .add(x)
# - itertools.chain.from_iterable
#

import utils
from itertools import chain
from utils import print_result


print("> Day 3")

#
# Part 1
#
def priority(char):
    o = ord(char)
    if o >= 97:
        return o - 96
    else:
        return o - 38


def dupes(elems):
    fst_half = set(elems[:len(elems) // 2])
    snd_half = set(elems[len(elems) // 2:])
    return [e for e in snd_half if e in fst_half]


def part_1(data):
    return sum(map(priority, list(chain.from_iterable((map(dupes, data))))))


test_data = utils.read_lines("data/day_03_test.txt")
print_result(1, part_1(test_data), True)

data = utils.read_lines("data/day_03.txt")
print_result(1, part_1(data))


#
# Part 2
#
def part_2(data):
    i = 0
    sum_priorities = 0
    while i + 2 <= len(data):
        s1 = data[i]
        s2 = data[i + 1]
        s3 = data[i + 2]
        common_elements = set([e for e in s1 if e in s2 and e in s3])
        sum_priorities += priority(next(iter(common_elements)))
        i += 3
    return sum_priorities

print_result(2, part_2(test_data), True)
print_result(2, part_2(data))

#
# People's solution
#
