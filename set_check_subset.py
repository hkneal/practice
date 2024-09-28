"""You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.
"""

if __name__ == "__main__":

    t_num = int(input().rstrip())

    for _ in range(t_num):
        ele_num_a = int(input().rstrip())
        a_set = set([int(x) for x in input().split(" ")])
        ele_num_b = int(input().rstrip())
        b_set = set([int(x) for x in input().split(" ")])
        diff_set = b_set.difference(a_set)
        b_set.difference_update(diff_set)

        if b_set == a_set:
            print(True)
        else:
            print(False)