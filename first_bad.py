import math
def isBadVersion(n: int) -> bool:
        return n>=4

class Solution:

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n+1
        while left < right:
            mid = math.floor((left + right)/2)
            if isBadVersion(mid):
                if mid == 1 or (mid-1 > 0 and not isBadVersion(mid-1)):
                    return mid
                right = mid
            else:
                left = mid
        return left

n = 5
print(Solution().firstBadVersion(n))