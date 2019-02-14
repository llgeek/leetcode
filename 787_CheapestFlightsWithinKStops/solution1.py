"""
use DFS, but with DP, to fix TLE problem in leetcode
"""

class Solution():
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        prices = [[[-1] * n for _ in range(n)] for _ in range(K)]
        for flight in flights:
            s, d, p = flight
            prices[s][d][0] = p
            for i in range(n):
                if prices[i][s] != -1:
                    prices[i][d] = min(prices[i][d], prices[i][s] + p)
            for j in range(n):
                if prices[d][j] != -1:
                    prices[s][j] = min(prices[s][j], prices[d][j]+ p)
        return prices[src][dst]