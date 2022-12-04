#!/usr/bin/env python3
#
# Day 4
#
# I wanted to avoid numpy (saving that for later ;)), rather than that, I wanted
# to learn more about python classes.
#
# Lessons learned:
# - simple class (that's why this solution is so long :) )
# - __repr__ (= .toString() in python)
# - types
# - pytest (setting the paths correctly was "fun")
#   - pytest.mark.parametrize looks nice!
#

from utils import print_result, read_lines
from typing import List



print("> Day 4")


#
# Part 1
#
lines_test = read_lines("data/day_04_test.txt")
lines = read_lines("data/day_04.txt")


class SimpleInterval:
    """Simple interval

    Arguments:
    start_incl -- start number (inclusive)
    end_incl -- end number (inclusive)
    """
    def __init__(self, start_incl, end_incl):
        self.start_incl = start_incl
        self.end_incl = end_incl


    def contains_interval(self, other):
        """Return True if this interval fully contains the other interval."""
        return self.start_incl <= other.start_incl and self.end_incl >= other.end_incl


    def overlaps_interval(self, other):
        if self.start_incl <= other.start_incl:
            return other.start_incl <= self.end_incl
        else:
            return self.start_incl <= other.end_incl


    @staticmethod
    def parse(line: str):
        return SimpleInterval(*map(int, line.split("-")))


    def __repr__(self):
        return f"<{self.start_incl}, {self.end_incl}>"


class Line:
    """Line consisting of 2 intervals"""

    def __init__(self, interval_1: SimpleInterval, interval_2: SimpleInterval):
        self.interval_1 = interval_1
        self.interval_2 = interval_2


    def is_contained(self) -> bool:
        """True if one interval contains the other."""
        return self.interval_1.contains_interval(self.interval_2) or \
             self.interval_2.contains_interval(self.interval_1)


    def is_overlapping(self) -> bool:
        """True if one interval overlaps other"""
        return self.interval_1.overlaps_interval(self.interval_2)


    @staticmethod
    def parse(line: str):
        interval_1, interval_2 = map(SimpleInterval.parse, line.split(","))
        return Line(interval_1, interval_2)


    def __repr__(self):
        return f"{self.interval_1} - {self.interval_2}"


def count_contained(lines):
    return len([l for l in lines if Line.parse(l).is_contained()])

print_result(1, count_contained(lines_test), True)
print_result(1, count_contained(lines))


#
# Part 2
#
def count_overlapping(lines):
    return len([l for l in lines if Line.parse(l).is_overlapping()])

print_result(2, count_overlapping(lines_test), True)
print_result(2, count_overlapping(lines))

#
# People's solution
#
# This is pretty cool :) https://github.com/ThePituLegend/advent-of-code/tree/2022/day4
# (but it seems he generates sets of numbers, like many other solutions, which i don't like)
#
