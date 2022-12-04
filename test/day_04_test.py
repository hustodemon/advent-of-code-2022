#!/usr/bin/env python3

from ../day_04 import SimpleInterval
import pytest

@pytest.mark.parametrize("i1", "i2", [(SimpleInteral(1, 3), SimpleInterval(1, 2))])
def test_contains_interval(i1, i2):
    assert True

def test_doesnt_contain_interval():
    assert False


def test_always_fails():
    assert True
