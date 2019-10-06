from typing import List
import random
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def findKth(i, j, K):
            if i > j: return 
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]
            mid = partion(i, j)
            if K < mid-i+1: findKth(i, mid-1, K)
            else: findKth(mid+1, j, K-(mid-i+1))

        def partion(i, j):
            pivot, oi = dist(i), i
            i += 1
            while True:
                if dist(i) <= pivot:
                    i += 1
                else:
                    points[i], points[j] = points[j], points[i]
                    j -= 1
                if i > j: break
            points[oi], points[i-1] = points[i-1], points[oi]
            return i-1
        findKth(0, len(points)-1, K)
        return points[:K]
