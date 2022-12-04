#!/usr/bin/env python3
#
# Day 4
#
# Lessons learned:
# - simple class
# - __repr__ (= .toString() in python)
# - types
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


    def intersect_interval(self, other):
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


    def has_redundant_interval(self) -> bool:
        """True if one interval contains the other."""
        return self.interval_1.contains_interval(self.interval_2) or \
             self.interval_2.contains_interval(self.interval_1)


    @staticmethod
    def parse(line: str):
        interval_1, interval_2 = map(SimpleInterval.parse, line.split(","))
        return Line(interval_1, interval_2)

    def __repr__(self):
        return f"{self.interval_1} - {self.interval_2}"



class Groups:
    """Groups of elves and their sections"""
    def __init__(self, lines: List[Line]):
        pass

#    @staticmethod
#    def parse(lines: str) -> List[Groups]:
#        for i in range(0, len(lines), 2):
#        return [Line.parse(l) for l in lines ]



#Line.parse("3-4,3-5").has_redundant_interval()
#Groups.parse(lines_test)

def count_overlapping(lines):
    return len([res for l in lines if (res := Line.parse(l)).has_redundant_interval()])

count_overlapping(lines)


# Part 2
#

#
# People's solution
#
