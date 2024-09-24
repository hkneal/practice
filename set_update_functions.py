if __name__ == "__main__":

    a_num = int(input().rstrip())
    a_set = set([int(x) for x in input().split(" ")])

    s_num = int(input().rstrip())
    for _ in range(s_num):
        command, value = input().split()
        b_set = set([int(x) for x in input().split(" ")])
        eval("a_set." + command + "(b_set)")

    print(sum(a_set))


"""
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 52, 24}
4
.update() - Update the set by adding elements from an iterable/another set.

intersection_update - Update the set by keeping only the elements found in it and an iterable/another set.

{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
Result is: {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
update
{66, 55}
Result is: {1, 2, 3, 4, 5, 6, 7, 8, 9, 66, 11, 55}

.difference_update() - Update the set by removing elements found in an iterable/another set.

symmetric_difference_update() - Update the set by only keeping the elements found in either set, but not in both.
{35, 7, 22, 58, 62}
Result is: {1, 2, 3, 4, 5, 6, 8, 9, 66, 11, 35, 22, 55, 58, 62}

difference_update() - as above, Update the set by removing elements found in an iterable/another set.
{66, 35, 11, 22, 55, 58, 62}
Result is: {1, 2, 3, 4, 5, 6, 8, 9}

"""