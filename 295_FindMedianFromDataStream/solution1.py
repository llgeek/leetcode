"""
use two heaps

minHeap and maxHeap

write more tidy code, without considering too much cases,
simplified from solution.py

just maintain the propertity len(maxHeap) = len(minHeap) or len(maxHeap) = len(minHeap)+1
"""

import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self):
        """
        :rtype: float
        """
        return -self.maxheap[0] if len(self.maxheap) > len(self.minheap) else (-self.maxheap[0] + self.minheap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
