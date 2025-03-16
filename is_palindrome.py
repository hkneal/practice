import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', "", s).lower()

        j = len(s)-1
        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j -=1
        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))