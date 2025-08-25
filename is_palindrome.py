import re
class Solution:
    def isPalindromea(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', "", s).lower()

        j = len(s)-1
        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j -=1
        return True

s = "A man, a plan, a canal: Panama"
# print(Solution().isPalindromea(s))

def isPalindrome(phrase: str):
    if len(phrase) < 2 and phrase.isalnum():
        return True

    phrase = re.sub(r'[^a-zA-Z0-9]', "", phrase).lower()
    print(phrase)

    return phrase == phrase[::-1]

phrase = "Taco cat."
phrase = "I love SQL <3"

print(isPalindrome(phrase))
