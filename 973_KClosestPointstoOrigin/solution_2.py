import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
      heap = []
      dist = lambda x: x[0] ** 2 + x[1] ** 2
      for point in points:
        heapq.heappush(heap, (-dist(point), point))
        if len(heap) > K:
          heapq.heappop(heap)
      return [point for _, point in heap]