from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs_map = [0 for _ in strs[0]]
        prefix_word = strs[0]
        strs.pop(0)

        strs.sort()
        lowest = min(len(word) for word in strs)


        prefix = ""
        break_loop = False

        print(strs)
        for word in strs:
            if break_loop:
                break
            i = 0
            for c in prefix_word:
                if i > lowest-1:
                    break
                if c != word[i]:
                    strs_map[i] = False
                    break_loop = True
                    break

                elif c == word[i]:
                    strs_map[i] = True
                i += 1

        print(strs_map)
        for i, val in enumerate(strs_map):
            if val:
                prefix += strs[0][i]
            else:
                break

        return prefix



strs = ["flower","flow","flight"]
# strs = ["cir","car"]
# strs = ["c","acc","ccc"]
# strs = ["reflower","flow","flight"]
# strs = ["a","a","b"]
strs = ["aac","cab","abb"]
print(Solution().longestCommonPrefix(strs))