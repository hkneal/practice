from typing import List
def longest_consec(nums: List[int]) -> int:
    total_max = 0
    nums.sort()
    max_set = []

    for i in range(len(nums)):
        if i + 1 < len(nums):
            if nums[i] == nums[i+1] - 1:
                max_set.append(nums[i])
                max_set.append(nums[i+1])
            else:
                if len(max_set) > 0:
                    max_set = list(set(max_set))
                total_max = max(total_max, len(max_set))
                max_set = []

    return total_max

num_lst = [100, 4, 200, 1, 3, 2]
print(longest_consec(num_lst))