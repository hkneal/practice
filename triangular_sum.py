import math

def triangular_sum(nums):
    if len(nums) == 1:
        return nums[0]

    while len(nums) > 1:
        for i in range(len(nums)-1):
            nums[i] = (nums[i] + nums[i+1]) % 10
        nums.pop()

    return nums[0]


def triangular_sum_most_efficient(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    total = 0
    for i in range(n):
        C = math.comb(n-1, i)
        total = (total + nums[i] * C) % 10

    return total

print(triangular_sum([1,3,5,7]))
print(triangular_sum_most_efficient([1,3,5,7]))