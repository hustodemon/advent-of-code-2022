#!/usr/bin/env python3
#
# Day X
#
# Lessons learned:
# -
#

from utils import print_result, read_lines


print("> Day 10")


def process_instructions(state_acc, instructions):
    """"
    As usual, state_acc carries over the solution at each step.
    It consists of 3 parts: (register state, cycle number, CRT character #/. (for part 2)).
    """
    if len(instructions) == 1:
        return state_acc

    reg, cycle, _ = state_acc[-1]
    fst, *rst = instructions

    cycle_mod = cycle % 40  # for part 2
    crt_char = "#" if reg in range(cycle_mod - 1, cycle_mod + 2) else "."

    match fst.split():
        case ["noop"]:
            state_acc.append((reg, cycle + 1, crt_char))
            return process_instructions(state_acc, rst)
        case ["addx", n]:  # just increase the cycle cnt and add do_addx
            rst.insert(0, f"do_addx {n}")
            state_acc.append((reg, cycle + 1, crt_char))
            return process_instructions(state_acc, rst)
        case ["do_addx", n]:  # increase cycle _and_ update register
            state_acc.append((reg + int(n), cycle + 1, crt_char))
            return process_instructions(state_acc, rst)


lines = read_lines("data/day_10.txt")
acc = process_instructions([(1, 0, '')], lines)
print_result(1, sum(acc[i - 1][0] * i for i in range(20, 221, 40)))

print("  - Part 2:")
for state in acc:
    _, cycle, char = state
    if (cycle - 1) % 40 == 0:
        print('')
    print(char, end='')


#
# People's solution
#
