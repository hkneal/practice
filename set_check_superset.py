"""
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.
"""
if __name__ == "__main__":

    a_set = set([int(x) for x in input().split(" ")])
    n = int(input().rstrip())
    is_true = True

    for _ in range(n):
        b_set = set([int(x) for x in input().split(" ")])
        intersect = a_set.intersection(b_set)
        if (len(a_set) <= len(b_set)) or not intersect == b_set:
            is_true = False
            break

    print(is_true)