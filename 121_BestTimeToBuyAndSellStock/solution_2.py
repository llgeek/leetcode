from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        res = 0
        while right < len(prices):
          if prices[left] < prices[right]:
            res = max(res, prices[right] - prices[left])
          else:
            left = right
          right += 1
        return res

if __name__ == "__main__":
    # prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    sol = Solution()
    print(sol.maxProfit(prices))
