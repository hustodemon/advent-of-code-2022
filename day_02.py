#!/usr/bin/env python3
#
# Day 2
#
# Lessons learned:
# - nothing
#

from utils import print_result

print("> Day 2")

rules = {
    # I choose you, Rock!
    "A X": 1 + 3,  # oponent chooses rock, i get 1 for rock and 3 for draw
    "B X": 1 + 0,  # etc.
    "C X": 1 + 6,

    #  Paper
    "A Y": 2 + 6,
    "B Y": 2 + 3,
    "C Y": 2 + 0,

    #  Scissors
    "A Z": 3 + 0,
    "B Z": 3 + 6,
    "C Z": 3 + 3,
}


#
# Part 1
#
def compute_scores(games, rules):
    return [rules[game] for game in games]


games_test = utils.read_lines("data/day_02_test.txt")
games = utils.read_lines("data/day_02.txt")
print_result(1, sum(compute_scores(games_test, rules)), True)
print_result(1, sum(compute_scores(games, rules)))


#
# Part 2
#
rules_2 = {
    # I gotta lose
    "A X": 3, # oponent chooses rock, i need to lose, so i need to choose scissors
    "B X": 1, # gotta choose rock
    "C X": 2, # gotta choose paper

    # I gotta get draw
    "A Y": 1 + 3,  # i choose rock
    "B Y": 2 + 3,  # i choose paper
    "C Y": 3 + 3,  # i choose scissors

    # I gotta win
    "A Z": 2 + 6,  # i choose paper
    "B Z": 3 + 6,  # i choose scissors
    "C Z": 1 + 6,  # i choose rock
}

print_result(2, sum(compute_scores(games_test, rules_2)), True)
print_result(2, sum(compute_scores(games, rules_2)), True)

#
# People's solution
#
# The most readable were also dict-based like mine.
#

