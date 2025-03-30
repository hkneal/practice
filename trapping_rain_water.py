from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_amount = 0
        n = len(height)

        left_pass = [0] * n
        right_pass = [0] * n
        left_pass[0] = height[0]
        right_pass[n -1] = height[n-1]

        max_height = height[0]
        for i in range(1, n):
            max_height = max(max_height, height[i])
            left_pass[i] = max(max_height, height[i])
        print(left_pass)

        max_height = height[n-1]
        for i in range(n-2, -1, -1):
            max_height = max(max_height, height[i])
            right_pass[i] = max(max_height, height[i])
        print(right_pass)

        for i in range(n):
            trapped_amount += min(left_pass[i], right_pass[i]) - height[i]
            print(trapped_amount)

        return trapped_amount





height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(Solution().trap(height))