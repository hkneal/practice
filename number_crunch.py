t = 2
t_lst = [10, 100]
for a0 in range(t):
    n = t_lst[a0]
    n = n  - 1
    sum3 = (3*(n//3)*(n//3+1))//2
    sum5 = (5*(n//5)*(n//5+1))//2
    sum15 =(15*(n//15)*(n//15+1))//2
    sum = sum3+sum5-sum15
    print(sum)

