#!/usr/bin/env python3
#
# Day 5
#
# Lessons learned:
# - destructuring
# - comprehension without []
# - itertools FTW again
# - reversed
# - some re stuff
# - joining strings with .join instead of reduce
# - weird stride syntax list[::2] # only even elems
#

from utils import print_result, read_str
from collections import deque
from itertools import islice
from functools import reduce
import re


print("> Day 5")


#
# Part 1 & 2
#

def add_crates_to_stacks(line:str, stack_acc):
    crates = list(islice(line, 1, len(line), 4))
    for i in range(len(crates)):
        crate = crates[i]
        # create a new stack, if not exists
        if i >= len(stack_acc):
            stack_acc.append(deque())
        if crate != " ":
            stack_acc[i].append(crate)


def parse_instr(instr_str):
    """Parse instruction like 'move 1 from 2 to 3, gives back a list of integers (how_many, from, to)."""
    regex = r"move\s([0-9]*)\sfrom\s([0-9]*)\sto\s([0-9]*)$"
    return map(int, re.match(regex, instr_str).groups())


def apply_instruction_part_1(how_many, from_where, to_where, stacks):  # from_where/to_where is not idx
    """Apply instruction to stacks"""
    for i in range(how_many):
        stacks[to_where - 1].append(stacks[from_where - 1].pop())


def apply_instruction_part_2(how_many, from_where, to_where, stacks):  # from_where/to_where is not idx
    """Apply instruction to stacks, for part 2"""
    elems = []
    for i in range(how_many):
        elems.append(stacks[from_where - 1].pop())
    for e in reversed(elems):
        stacks[to_where - 1].append(e)


def compute(path, apply_instruction_fn):
    # some processing first
    crate_strings, instruction_strings = read_str(path).split("\n\n")
    crate_layers = crate_strings.splitlines()
    crate_layers = crate_layers[:-1]  # we don't care about the stack names (1, 2, 3...)
    instruction_strings = instruction_strings.splitlines()

    # initialize: fill the stacks
    stack_acc = []
    for crate_row in reversed(crate_layers):
        add_crates_to_stacks(crate_row, stack_acc)

    # apply the instructions
    for instr_str in instruction_strings:
        instr = parse_instr(instr_str)
        apply_instruction_fn(*instr, stack_acc)

    #return reduce(lambda s1, s2: s1 + s2, [s.pop() for s in stack_acc]);
    return "".join(s.pop() for s in stack_acc)

print_result(1, compute("data/day_05_test.txt", apply_instruction_part_1), True)
print_result(1, compute("data/day_05.txt", apply_instruction_part_1))

print_result(2, compute("data/day_05_test.txt", apply_instruction_part_2), True)
print_result(2, compute("data/day_05.txt", apply_instruction_part_2))

#
# People's solution
#
#a really condensed one :)
#S, I = open('in.txt').read().split('\n\n')
#for dir in -1, +1:
#    s = [['']]+[''.join(s).strip() for s in zip(*S.split('\n'))][1::4]
#    for i in I.split('\n'):
#        n, a, b = map(int, i.split()[1::2])
#        s[b] = s[a][:n][::dir] + s[b]
#        s[a] = s[a][n:]
#
#    print(*[*zip(*s)][0], sep='')
#
#other one:
#sanitise input
#stacks, instructions = lines.split("\n\n")
#stacks = stacks.splitlines()
#instructions = instructions.splitlines()
#print("\n".join(stacks))
#trans = list(map(list, zip(*stacks)))
#stacks = [list("".join(x[:-1][::-1]).strip()) for x in trans[1::4]]
#stacks1, stacks2 = 2 * [stacks.copy()]
#solution 1
#for instr in list(map(lambda x: x.split(), instructions)):
#    N, fro, to = map(int, instr[1::2])
#
#    stacks1[to - 1].extend(stacks1[fro - 1][-N:][::-1])
#    del stacks1[fro - 1][-N:]
#
#"".join([x[-1] for x in stacks1])
#solution 2
#for instr in list(map(lambda x: x.split(), instructions)):
#    N, fro, to = map(int, instr[1::2])
#
#    stacks2[to - 1].extend(stacks2[fro - 1][-N:])
#    del stacks2[fro - 1][-N:]
#
#"".join([x[-1] for x in stacks2])
