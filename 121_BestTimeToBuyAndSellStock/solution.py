class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        minprice = float('inf')
        maxprofit = 0
        for p in prices:
            if p < minprice:
                minprice = p 
            else:
                maxprofit = max(maxprofit, p - minprice)
        return maxprofit

    
if __name__ == "__main__":
    # prices = [7,1,5,3,6,4]
    # prices = [7, 6, 4, 3, 1]
    prices = [2, 1, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
