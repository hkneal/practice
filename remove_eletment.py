from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        head = 0
        for ind, value in enumerate(nums):
            if value is not val:
                nums[head] = nums[ind]
                head += 1
        return head


nums = [3,2,2,3]
val = 3

print(Solution().removeElement(nums, val))