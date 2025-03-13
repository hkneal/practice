from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count_map = {}

        for ind, val in enumerate(nums):
            if ind == 0 or ind == 1:
                nums[i] = val
                if val in count_map:
                    count_map[val] += 1
                else:
                    count_map[val] = 1
                i += 1

            elif val in count_map:
                if count_map[val] < 2:
                    count_map[val] += 1
                    nums[i] = val
                    i += 1

            else:
                count_map[val] = 1
                nums[i] = val
                i += 1
        return i



nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))