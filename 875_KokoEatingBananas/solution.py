"""
binary search
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum((p-1)//K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid 
            else:
                lo = mid+1
        return lo