from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # map of values
        nums_map = {}
        out = []
        for ind in range(len(nums)):
            diff = abs(nums[ind] - target)
            nums_map[ind] = diff
        print(f'Nums_map: {nums_map}')

        for key, val in nums_map.items():
            print(val)
            if val + nums[key] == target:
                ind = list(nums_map.keys()).index(abs(target - val))
                print(key, nums_map[ind])
                out = [key, 1]
                return out
    
        return out

nums = [2,7,11,15]
sol = Solution()
sol.twoSum(nums, 9)

        