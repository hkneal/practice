"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321
"""
x = 5
for i in range(1, x+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # print(''.join([str(x) for x in range(1, i+1)]),''.join([str(x) for x in range(i-1, 0, -1)]), sep="")
    print(sum(list(map(lambda x: 1*10**x, range(i))))**2)

for i in range(1, i):
    print(11*i-10)