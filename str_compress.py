"""Practicing problem solving"""


if __name__ == "__main__":
    s = input()
    ptr = 0
    next = 1
    count = 1
    tuple_lst = []

    while next < len(s):
        if s[next] == s[ptr]:
            count += 1
            next +=1
        else:
            tuple_lst.append(tuple([count, int(s[ptr])]))
            ptr = next
            next += 1
            count = 1

    tuple_lst.append(tuple([count, int(s[ptr])]))

    for tup in tuple_lst:
        print(tup, end=" ")