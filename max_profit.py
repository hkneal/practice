from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = -float('inf')
        max_profit = 0
        for price in prices:
            buy = max_profit - price
            hold = cost
            sell = cost + price
            avoid = max_profit

            cost = max(buy, hold)
            max_profit = max(sell, avoid)
        return max_profit


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))


# def maxProfit(self, prices: List[int]) -> int:
#         cost = float('inf')
#         max_profit = 0
#         for price in prices:
#             if price < cost:
#                 cost = price
#             else:
#                 max_profit = max(max_profit, price - cost)
#         return max_profit
