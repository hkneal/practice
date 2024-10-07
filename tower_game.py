def towerBreakers(n, m):
    # Write your code here
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1

if __name__ == '__main__':
    n = 100001
    m = 1
    result = towerBreakers(n, m)
    print(result)

