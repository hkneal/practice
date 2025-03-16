class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer = 0
        tpointer = 0

        for i in range(len(t)):
            if s[spointer] == t[tpointer]:
                spointer += 1
                tpointer += 1

            else:
                tpointer += 1

            if spointer > len(s)-1:
                break

        # while spointer <= len(s) - 1 and tpointer <= len(t) -1:
        #     if s[spointer] == t[tpointer]:
        #         spointer += 1
        #         tpointer += 1

        #     else:
        #         tpointer += 1
        return spointer > len(s) - 1

# s = "abc"
# t = "ahbgdc"
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))