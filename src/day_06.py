#!/usr/bin/env python3
#
# Day 6
#
# Lessons learned:
# -
#

from utils import print_result, read_str


print("> Day 6")


#
# Part 1
#
def compute(signal, marker_len = 4):
    return [i for i in range(marker_len, len(signal) - 1)
            if len(set(signal[i-marker_len:i])) == marker_len][0]


test_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
input = read_str("data/day_06.txt")
print_result(1, compute(test_input), True)
print_result(1, compute(input), True)

#
# Part 2
#
print_result(2, compute(test_input, 14), True)
print_result(2, compute(input, 14), True)

#
# People's solution
#
# IMvHO the nicest solutions were quite similar to this one
#
