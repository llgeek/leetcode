"""
use two heaps

minHeap and maxHeap
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
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.minheap, num)
            return 
        if not self.maxheap:
            if num > self.minheap[0]:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
            return
        if len(self.maxheap) == len(self.minheap):
            if num < -self.maxheap[0]:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        elif len(self.maxheap) > len(self.minheap):
            if num < -self.maxheap[0]:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        else:
            if num > self.minheap[0]:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()