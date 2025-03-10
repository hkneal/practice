from math import ceil, sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False

        for i in range(2, int(ceil(sqrt(n)))):
            if primes[i]:
                for mul_of_i in range(i*2, n, i):
                    primes[mul_of_i] = False

        return sum(primes)

print(Solution().countPrimes(34))