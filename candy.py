from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        candy_cost = [1] * len(ratings)

        for i in range(1, len(ratings)):

            # check left to right
            if ratings[i-1] < ratings[i]:
                candy_cost[i] = candy_cost[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            # check right to left
            if ratings[i] > ratings[i+1]:
                if candy_cost[i] <= candy_cost[i+1]:
                    candy_cost[i] = candy_cost[i+1] + 1

        return sum(candy_cost)

ratings = [1,3,2,4,3,2,1,3,2]
print(Solution().candy(ratings))