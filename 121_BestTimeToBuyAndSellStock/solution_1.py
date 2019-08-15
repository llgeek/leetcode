from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, ans = 0, 0
        for right, val in enumerate(prices):
            if val > prices[left]:
                ans = max(ans, val-prices[left])
            if val < prices[left]:
                left = right
        return ans
