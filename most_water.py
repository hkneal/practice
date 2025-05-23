from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1


        while left < right:
            print(f'Left: {left}, Right: {right}, Maxarea: {max_area}')
            max_area = max(max_area, (min(height[left], height[right]) * (right - left)))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area



test_arr = [8,7,2,1]
print(Solution().maxArea(test_arr))