"""Practicing with itertools"""

import itertools


line = input()
input_lst = line.split(" ")

permutations = itertools.permutations(input_lst[0], int(input_lst[1]))
permutations_list = sorted(["".join(x) for x in permutations])

for _ in permutations_list:
    print(_)