from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return 0

        target = len(nums) -1
        index = 0
        longest_index = 0
        no_of_jumps = 0

        for i in range(len(nums)-1):
            longest_index = max(longest_index, i + nums[i])
            if i == index:
                no_of_jumps += 1
                index = longest_index

                if index >= target:
                    break

        return no_of_jumps

nums = [2,3,1,1,4, 1, 1, 1, 1]
# nums = [3,2,1,0,4]
# nums = [1]
# nums = [2,0,0]
print(Solution().canJump(nums))

# Optimal Greedy O(n) solution:
# def canJump(self, nums: List[int]) -> bool:
#         target = len(nums) -1

#         for i in range(len(nums)-1, -1, -1):
#             if i + nums[i] >= target:
#                 target = i

#         return target == 0

# Top down dp memoization
# def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True

#         target = len(nums) -1

#         @lru_cache(maxsize=None)
#         def jump_at_ind(ind: int) -> bool:

#             if ind == target:
#                 return True

#             for i in range(1, nums[ind]+1):
#                 if jump_at_ind(ind + i):
#                     return True

#             return False


#         return jump_at_ind(0)