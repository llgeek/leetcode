import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left, self.right = [], []

        

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, num)
        elif len(self.left) < len(self.right):
            if self.right[0] >= num:
                heapq.heappush(self.left, -num) 
            else:
                heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
        else:
            if -self.left[0] <= num:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()