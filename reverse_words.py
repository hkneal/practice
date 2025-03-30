class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(None, s.strip().split(" ")[::-1]))



s = "  hello world  "
s = "a good   example"
print(Solution().reverseWords(s))