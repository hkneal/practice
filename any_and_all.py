# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    palindromes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    n, lst = int(input().rstrip()), [int(x) for x in input().split()]
    print(True if (all([True if x >=0 else False for x in lst]) and any([x for x in lst if x in palindromes])) else False)