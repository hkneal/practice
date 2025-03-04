from typing import List
nums = [3,0, 1]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Using Gauss's Formula
        n = len(nums)
        expected_sum = int(n*(n+1)/2)
        acual_sum = sum(nums)
        return expected_sum - acual_sum

        # Answer using sets
        # set_nums = set(nums)
        # set_compare = set([x for x in range(len(nums)+1)])
        # return set_compare.difference(set_nums).pop()


        #Also works
        # for num in range(len(nums)+1):
        #     if num not in nums:
        #         return num




# print([x for x in range(len(nums)+1)])
print(Solution().missingNumber(nums))