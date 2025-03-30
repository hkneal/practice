from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        longest = min(len(word) for word in strs)

        prefix = prefix[:longest]

        # print(f"Prefix Word: {prefix}")
        for word in range(1, len(strs)):

            while not strs[word].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix



strs = ["flower","flow","flight"]
strs = ["cir","car"]
strs = ["c","acc","ccc"]
# strs = ["reflower","flow","flight"]
# strs = ["a","a","b"]
strs = ["aac","cab","abb"]
print(Solution().longestCommonPrefix(strs))