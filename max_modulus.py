"""Get the higest mod value possible"""
from itertools import product


if __name__ == "__main__":
    n, m = (int(x) for x in input().split())
    matrix = []

    for _ in range(n):
        lst = [ int(x) for x in input().rsplit()]
        lst.pop(0)
        matrix.append(lst)

    matrix = list(product(*matrix))

    max = 0

    for tup in matrix:
        val = (sum([x**2 for x in tup]) % m)
        if val > max:
            max = val

    print(max)


"""
6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304
"""