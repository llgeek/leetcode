import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda x: x[0]**2 + x[1]**2
        heap = []
        for point in points:
          heapq.heappush(heap, (-dist(point), point))
          if len(heap) > K:
            heapq.heappop(heap)
        return [ele[1] for ele in heap]
