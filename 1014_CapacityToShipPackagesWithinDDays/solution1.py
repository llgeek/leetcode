"""
binary search

"""

class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        def possible(K):
            day = 0
            curval = 0
            for val in weights:
                if curval + val <= K:
                    curval += val
                else:
                    day += 1
                    curval = val
            day += (curval != 0)
            return day <= D 

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

