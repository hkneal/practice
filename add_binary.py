class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = bin(int(a, 2) + int(b, 2))
        return bin_sum[2:]


a = "1010"
b = "1011"
print(Solution().addBinary(a, b))