"""
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices
(assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""
import itertools, math
if __name__ == "__main__":

    count = 0
    n = int(input().rstrip())
    lst = [x for x in input().split(" ")]
    k = int(input().rstrip())
    combos = itertools.combinations(lst, k)

    for combo in combos:
        if 'a' in combo:
            count += 1
    if count > 0:
        print(count / math.comb(n, k))
    else:
        print(0)