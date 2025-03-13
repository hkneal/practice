from typing import List
import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = math.ceil(k%len(nums))
        if k > 0:
            begining = nums[-k:]
            nums[:] = begining + nums[0:len(nums)-k]


        print(k)
        #     begining = nums[-k:]
        #     nums[:] = begining + nums[0:len(nums)-k]
        print(nums)

nums = [-1,-100,3,99]
nums = [1,2,3,4,5,6,7]
nums = [1,2]
nums = [-1]
k = 2
Solution().rotate(nums, k)