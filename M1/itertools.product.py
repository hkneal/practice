"""
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
"""

import sys, itertools

tuple_list = []

# Read multiple lines
for line in sys.stdin:
    tuples = tuple(line.strip('\n').split(" "))
    tuple_list.append(tuples)

product = itertools.product(tuple_list[0], tuple_list[1])
for t in product:
    print((int(t[0]), int(t[1])), end=" ")
