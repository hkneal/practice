if __name__ == "__main__":

    x, k = (int(x) for x in input().split())
    my_function = input()
    if eval(my_function) == k:
        print(True)
    else:
        print(False)