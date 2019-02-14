class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = [(point[0]**2 + point[1]**2, point[0], point[1])for point in points]
        heapq.heapify(heap)
        return [list(heapq.heappop(heap)[1:])for _ in range(K)]
        