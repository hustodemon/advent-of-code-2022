#!/usr/bin/env python3
#
# Day 1
#
# Lessons learned:
# - f-strings
# - list comprehensions (see below)
# - default args (print function)
# - with open('bla') as bleh:
#

from utils import print_result


print("> Day 1")


def compute_sums(lines):
    idx = 0
    sums = [0]
    for l in lines:
        if l == '':
            idx += 1
            sums.append(0)
        else:
            sums[idx] += int(l)
    return sums


#
# Part 1
#
lines_test = utils.read_lines("data/day_01_test.txt")
sums_test = compute_sums(lines_test)
print_result(1, str(max(*sums_test)), True)

lines = utils.read_lines("data/day_01.txt")
sums = compute_sums(lines)
print_result(1, str(max(*sums)))


#
# Part 2
#
print_result(2, sum(sorted(sums_test, reverse=True)[:3]), True)
print_result(2, sum(sorted(sums, reverse=True)[:3]))

#
# Mostly ppl in reddit used approach like that:
# IDK, which is uglier
#
#[sum(map(int, [x for x in cal_grp.split("\n") if x != '']))
#  for cal_grp in open("data/day_01_test.txt").read().split("\n\n")]
#
