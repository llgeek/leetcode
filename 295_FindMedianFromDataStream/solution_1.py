"""
second trial

MinHeap and MaxHeap
"""

import heapq

class MedianFinder(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap)+1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
