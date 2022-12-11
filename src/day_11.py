#!/usr/bin/env python3
#
# Day 11
#
# Lessons learned:
# - some class stuff, some types, eval :D
#

from utils import print_result, read_str
from operator import mul
from functools import reduce


print("> Day 11")

monkey_txts_test = read_str("data/day_11_test.txt").split("\n\n")
monkey_txts = read_str("data/day_11.txt").split("\n\n")

class Monkey():


    def __init__(self, string: str):
        self._parse(string.splitlines())


    def _parse(self, lines: list[str]):
        id_line, items_line, operation_line, test_line, true_line, false_line = lines
        self.id = id_line.split(" ")[1][:-1]
        items_str = items_line.split(":")[1].strip()
        self.items = list(map(int, map(str.strip, items_str.split(","))))
        self.operation = operation_line.split("new =")[1].strip()
        self.test_divisible_by = int(test_line.split("divisible by")[1].strip())
        self.throw_to_monkey = {
            True: int(true_line.split("throw to monkey")[1].strip()),
            False: int(false_line.split("throw to monkey")[1].strip()),
        }
        self.num_of_inspections = 0


    def turn(self, monkies, adjust_worry_lvl_fn):
        self.num_of_inspections += len(self.items)
        for item in self.items:
            old = item
            worry_lvl = eval(self.operation)  # YOLOOOOO eval!
            worry_lvl = adjust_worry_lvl_fn(worry_lvl)
            throw_monkey = self.throw_to_monkey[worry_lvl % self.test_divisible_by == 0]
            monkies[throw_monkey].items.append(worry_lvl)
        self.items = []


    def __repr__(self):
        return (
            f"Id: {self.id}\n"
            f"Items: {self.items}\n"
            f"Operation: {self.operation}\n"
            f"Test divisible by: {self.test_divisible_by}\n"
            f"If true, throw to : {self.throw_to_monkey[True]}\n"
            f"If false, throw to : {self.throw_to_monkey[False]}\n"
            f"Num of inspections : {self.num_of_inspections}\n"
        )


def part_1(monkey_txts):
    worry_lvl_adjust = lambda x: x // 3
    monkies = [Monkey(s) for s in monkey_txts]
    for round in range(0, 20):
        for monkey in monkies:
            monkey.turn(monkies, worry_lvl_adjust)
    return mul(*sorted([m.num_of_inspections for m in monkies])[-2:])

print_result(1, part_1(monkey_txts_test), True)
print_result(1, part_1(monkey_txts), True)


def part_2(monkey_txts):
    monkies = [Monkey(s) for s in monkey_txts]
    common_multiple = reduce(mul, [m.test_divisible_by for m in monkies])
    worry_lvl_adjust = lambda x: x % common_multiple
    for round in range(0, 10000):
        for monkey in monkies:
            monkey.turn(monkies, worry_lvl_adjust)
    return reduce(mul, sorted([m.num_of_inspections for m in monkies])[-2:])

print_result(2, part_2(monkey_txts_test), True)
print_result(2, part_2(monkey_txts), True)

#
# People's solution
#
