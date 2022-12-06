#!/usr/bin/env python3


def read_lines(path):
    """
    Read a file and split it by lines.
    """
    with open(path, "r") as f:
        return f.read().splitlines()


def read_str(path):
    """
    Read a file into a string and return it.
    """
    with open(path, "r") as f:
        return f.read()


def print_result(part, s, is_test=False):
    """
    Print result of a puzzle part.
    """
    print(f"  - Part {part} {'(test set)' if is_test else ''}: {s}")
