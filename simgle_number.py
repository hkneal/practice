from typing import List
class Solution:
    #Using xor
    def singleNumber(self, nums: List[int]) -> int:
        val = 0
        for num in nums:
            val ^= num
        return val


nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))




# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         expected_sum = 2*(sum(set(nums)))
#         return expected_sum - sum(nums)