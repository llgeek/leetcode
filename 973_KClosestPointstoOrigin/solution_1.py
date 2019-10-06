from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            if len(heap) < K:
                heapq.heappush(heap, (-dist, point))
            else:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, point))
        return [val[1] for val in heap]
