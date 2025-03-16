from typing import List
from functools import reduce
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*(len(nums))
        #Calculate prefix
        # for i in range(len(nums)):
        #     if i == 0:
        #         output[i] = 1  * nums[i]
        #     else:
        #         output[i] = output[i-1] * nums[i]
        # print(output)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix      # output = [1, 1, 2, 6]
            prefix *= nums[i]       # prefix = 1 * 2 = 2,
        print(output)
        #Calculate postfix & result
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        print(output)
        return output

        # def get_product(lst: List[int]) -> int:
        #     return math.prod(lst)



data = [1,2,3,4]
Solution().productExceptSelf(data)