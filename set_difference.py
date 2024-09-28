if __name__ == "__main__":

    e_num = int(input().rstrip())
    e_set = set([int(x) for x in input().split(" ")])

    f_num = int(input().rstrip())
    f_set = set([int(x) for x in input().split(" ")])

    print(len(e_set.difference(f_set)))