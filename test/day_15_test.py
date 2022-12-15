#!/usr/bin/env python3

import sys
sys.path.append('src')

import day_15
from utils import read_str
import pytest


@pytest.mark.parametrize("a, b, expected", [
    ((0, 0), (2,0), 2),
    ((0, 0), (2,2), 4),
    ((0, 0), (-2,2), 4),
    ((-1, -2), (1,2), 6),
    ((2, 18), (-2, 15), 7),
])
def test_manhattan_distance(a, b, expected):
    assert day_15.manhattan_distance(a, b) == expected


@pytest.mark.parametrize("pt, dist, expected_pts", [
    ((1,1), 1, set([(0, 1), (2, 1), (1, 0), (1, 2), (1, 1)]))
])
def test_generator_points(pt, dist, expected_pts):
    assert day_15.gen_points_at_distance(pt, dist) == expected_pts


@pytest.mark.parametrize("pt, dist, expected_count", [
    ((1,1), 1, 5),
    ((-1,-1), 2, 13),
])
def test_generator_points_count(pt, dist, expected_count):
    assert len(day_15.gen_points_at_distance(pt, dist)) == expected_count
