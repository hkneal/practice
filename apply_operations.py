from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        ind = 0

        #Apply Operation
        for i, num in enumerate(nums):
            if i < len(nums) -1:
                if nums[i+1] == num:
                    nums[i]*=2
                    nums[i+1] = 0

        #Shift zeros
        for num in nums:
            if num != 0:
                nums[ind] = num
                ind += 1

        for i in range(ind, len(nums)):
            nums[i] = 0

        return nums

nums = [0,1]
print(Solution().applyOperations(nums))
