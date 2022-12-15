#!/usr/bin/env python3

import sys
sys.path.append('src')

from day_11 import Monkey
from utils import read_str
import pytest


def test_parse_monkey():
    fst_monkey_str = read_str("data/day_11_test.txt").split("\n\n")[0]
    fst_monkey = Monkey(fst_monkey_str)
    assert fst_monkey.items == [79, 98]
    assert fst_monkey.operation == "old * 19"
    assert fst_monkey.test_divisible_by == 23
    assert fst_monkey.throw_to_monkey == {True: 2, False: 3}

