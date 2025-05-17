def sum(n: int) -> int:
    if n <= 0:
        return 0
    return n + sum(n -1)


print(sum(3))


def sum_all(a, b, c, d, e):
    print(a, b, c, d, e)
    return (a + b + c + d + e)


params = {
    "e": 5,
    "b": 2,
    "c": 1,
    "a": 6,
    "d": 7
}

print(sum_all(**params))