import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = Counter(S)
        heap = [(-value, key) for key, value in cnt.items()]
        heapq.heapify(heap)
        if (-heap[0][0]) * 2 > len(S) + 1: 
            return ""
        ans = []
        while len(heap) >= 2:
            nct1, chr1 = heapq.heappop(heap)
            nct2, chr2 = heapq.heappop(heap)
            ans.extend([chr1, chr2])
            if nct1 + 1: heapq.heappush(heap, (nct1 + 1, chr1))
            if nct2 + 1: heapq.heappush(heap, (nct2 + 1, chr2))
        return "".join(ans) + (heap[0][1] if heap else "")

