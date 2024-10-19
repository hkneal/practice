"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
# from typing import List

class Solution:
    def twoSum(self, nums, target: int):

        # Smarter solution:

        for i, num in enumerate(nums):
            diff = abs(target - num)
            if diff in nums and nums.index(diff) != i:
                return nums.index(diff), i

        return None, 0


        # map of values
        # nums_map = {}
        # out = []
        # for ind in range(len(nums)):
        #     diff = abs(nums[ind] - target)
        #     nums_map[ind] = diff
        # print(f'Nums_map: {nums_map}')

        # for key, val in nums_map.items():
        #     print(val)
        #     if val + nums[key] == target:
        #         ind = list(nums_map.keys()).index(abs(target - val))
        #         print(key, nums_map[ind])
        #         out = [key, 1]
        #         return out

        # return out

nums = [2,7,11,15]
sol = Solution()
print(sol.twoSum(nums, 9))

