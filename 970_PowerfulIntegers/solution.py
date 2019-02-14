"""
use priority, can maintain the order

TLE in leetcode, priority requires lots of additional work
"""


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        import heapq
        heap = []
        res = set()
        ret = []
        heapq.heappush(heap, (x+1, x, 1, 1, 0))
        heapq.heappush(heap, (1+y, 1, y, 0, 1))
        heapq.heappush(heap, (1+1, 1, 1, 0, 0))
        while heap:
            val, xx, yy, i, j = heapq.heappop(heap)
            if val <= bound:
                if val not in res:
                    res.add(val)
                    ret.append(val)
                heapq.heappush(heap, (xx*x+yy, xx*x, yy, i+1, j))
                heapq.heappush(heap, (xx+yy*y, xx, yy*y, i, j+1))
        return ret

if __name__ == "__main__":
    x = 1
    y = 2
    bound = 100
    sol = Solution()
    print(sol.powerfulIntegers(x, y, bound))
        
