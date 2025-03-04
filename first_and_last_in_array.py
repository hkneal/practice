from typing import List
import math

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target < nums[0] or target > nums[len(nums)-1]:
            return [-1, -1]

        #Using binary search
        left_index = self.__find_left(nums, target)
        right_index = self.__find_right(nums, target)
        return [left_index, right_index]

    def __find_left(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = math.floor((right + left)/2)
            if nums[mid] == target :
                if mid == 0 or nums[mid-1] != target:
                    return mid
                right = mid -1
            elif nums[mid] > target:
                right = mid -1
            else: left = mid + 1
        return -1

    def __find_right(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = math.floor((right + left)/2)
            if nums[mid] == target :
                if mid == len(nums) -1 or nums[mid+1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else: right = mid - 1
        return -1


nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))

# def searchRange(self, nums: List[int], target: int) -> List[int]:
#         nums_length = len(nums) -1
#         try:
#             first_ind = nums.index(target)
#             last_ind = nums[::-1].index(target)
#         except Exception:
#             return [-1, -1]
#         last_ind = nums_length - last_ind

#         return [first_ind, last_ind]

# def searchRange(self, nums: List[int], target: int) -> List[int]:
#         ans = []
#         while target in nums:
#             i = nums.index(target)
#             ans.append(nums.index(target))
#             nums[i] = 'x'
#         if len(ans) == 1:
#             ans.append(ans[0])
#         if not ans:
#             return [-1, -1]
#         else:
#             ans =[ans[0], ans[len(ans)-1]]
#             return ans