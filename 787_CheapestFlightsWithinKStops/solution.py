"""
use DFS, but TLE in leetcode

can optimize code with DP
"""


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        if src == dst:
            return 0
        adjmat = {}
        for flight in flights:
            if flight[0] not in adjmat:
                adjmat[flight[0]] = [(flight[1], flight[2])]
            else:
                adjmat[flight[0]].append((flight[1], flight[2]))
        stack = []
        cheapest = (1<<31)-1
        stack.append((src, -1, 0))
        while stack:
            node, depth, accprice = stack.pop()
            if depth > K or (depth == K and node != dst):
                continue
            if node == dst:
                cheapest = min(cheapest, accprice)
            else:
                if node in adjmat:
                    for adjnode in adjmat[node]:
                        stack.append((adjnode[0], depth+1, accprice+adjnode[1]))
        return -1 if cheapest == (1<<31)-1 else cheapest

if __name__ == "__main__":
    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # K = 0
    n = 5
    flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    src = 2
    dst = 1
    K = 1
    sol = Solution()
    print(sol.findCheapestPrice(n, flights, src, dst, K))
            
            
