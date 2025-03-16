from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort(reverse=True)
        print(citations)

        for i, val in enumerate(citations):
            if val >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index

citations = [3,0,6,1,5]
print(Solution().hIndex(citations))