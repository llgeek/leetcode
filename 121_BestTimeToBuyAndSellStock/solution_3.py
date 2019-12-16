class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice, maxprofit = (1<<31) - 1, 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if maxprofit < prices[i] - minprice:
                maxprofit = prices[i] - minprice
        return maxprofit