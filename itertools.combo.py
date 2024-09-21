"""Prints all the combinations of string S up to size K in lexicographic sorted order"""

import itertools
if __name__ == "__main__":
    s, k = input().split()
    k = int(k)
    s_lst = []

    for i in range(1, k+1):
        s_lst += sorted(["".join(x) for x in itertools.combinations(sorted(list(s)), i)])

    for _ in (s_lst):
        print(_)