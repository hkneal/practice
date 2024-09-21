"""Calculate your happiness"""

n, m = input().split()
arr = input().split()
happy_set = set(input().split())
unhappy_set = set(input().split())
happy = 0

for val in arr:
    if val in happy_set:
        happy += 1
    elif val in unhappy_set:
        happy -= 1


print(happy)