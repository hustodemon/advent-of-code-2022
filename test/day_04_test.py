#!/usr/bin/env python3

import sys
sys.path.append('src')  # you must be kidding me. is this how it's done?
# seems the tests then needs to me run from the base dir

from day_04 import SimpleInterval
import pytest

@pytest.mark.parametrize("i1, i2", [
    (SimpleInterval(1, 3), SimpleInterval(1, 2)),
    (SimpleInterval(1, 3), SimpleInterval(1, 2)),
    (SimpleInterval(-2, 4), SimpleInterval(-1, 3)),
])
def test_contains_interval(i1, i2):
    assert i1.contains_interval(i2)


@pytest.mark.parametrize("i1, i2", [
    (SimpleInterval(1, 2), SimpleInterval(1, 3)),
    (SimpleInterval(0, 40), SimpleInterval(-2, -1)),
    (SimpleInterval(0, 40), SimpleInterval(50, 60)),
    (SimpleInterval(0, 40), SimpleInterval(-10, 10)),
    (SimpleInterval(0, 40), SimpleInterval(10, 60)),
])
def test_doesnt_contain_interval(i1, i2):
    assert not i1.contains_interval(i2)


@pytest.mark.parametrize("i1, i2", [
    (SimpleInterval(1, 2), SimpleInterval(1, 3)),
    (SimpleInterval(1, 3), SimpleInterval(1, 2)),
    (SimpleInterval(1, 100), SimpleInterval(2, 3)),
    (SimpleInterval(2, 3), SimpleInterval(1, 100)),
])
def test_interval_overlap(i1, i2):
    assert i1.overlaps_interval(i2)


@pytest.mark.parametrize("i1, i2", [
    (SimpleInterval(1, 2), SimpleInterval(3, 4)),
    (SimpleInterval(3, 4), SimpleInterval(1, 2)),
])
def test_interval_doesnt_overlap(i1, i2):
    assert not i1.overlaps_interval(i2)
