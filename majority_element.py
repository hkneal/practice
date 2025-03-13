from typing import List
from functools import lru_cache

@lru_cache
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        major = 0
        for num in nums:
            count = nums.count(num)
            if  count > max_count:
                max_count = count
                major = num

        return major


nums = [3,2,3]
print(Solution().majorityElement(nums))