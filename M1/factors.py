import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        factors = [x for x in range(1, n+1) if n % x == 0]
        print(factors)
        if k > len(factors):
            return -1
        return factors[k-1]



print(Solution().kthFactor(4, 4))