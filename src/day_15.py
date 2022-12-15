#!/usr/bin/env python3
#
# Day 15
#
# Lessons learned:
# -
#

from utils import print_result, read_lines
import re
import operator as op
from pprint import pprint
from itertools import chain


print("> Day 15")


#line = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
lines_test = read_lines("data/day_15_test.txt")
lines = read_lines("data/day_15.txt")


def parse_line(s):
    regex = r"Sensor at x=([^,]*), y=([^:]*): closest beacon is at x=([^,]*), y=(.*)"
    sx, sy, bx, by =  map(int, re.match(regex, s).groups())
    return ((sx, sy), (bx, by))


def manhattan_distance(a, b):
    return sum(map(abs, map(op.sub, a, b)))


def gen_points_up_to_distance(pt, dist, row=None):
    pt_x, pt_y = pt
    return set(
        (x, y)
        for x in range(pt_x - dist, pt_x + dist + 1)
        for y in [row or range(pt_y - dist, pt_y + dist + 1)]
        if manhattan_distance(pt, (x, y)) <= dist
    )


def part_1(lines, row_to_check):
    pts = set()
    beacons = set(parse_line(l)[1] for l in lines)
    for line in lines:
        sensor, beacon = parse_line(line)
        dist = manhattan_distance(sensor, beacon)
        pts.update(gen_points_up_to_distance(sensor, dist, row_to_check))

    pts_row = [pt for pt in pts if pt[1] == row_to_check and pt not in beacons]
    return len(pts_row)

print_result(1, part_1(lines_test, 10), True)
print_result(1, part_1(lines, 2000000))

#
# People's solution
#
