from collections import deque
from typing import List
class MonoQueue:
    def __init__(self):
        self.queue = deque()
    def push(self, val):
        cnt = 0
        while self.queue and self.queue[-1][0] < val:
            cnt += self.queue[-1][1] + 1
            self.queue.pop()
        self.queue.append((val, cnt))
    
    def pop(self):
        if not self.queue:
            return
        if self.queue[0][1] > 0:
            self.queue[0] = (self.queue[0][0], self.queue[0][1] - 1)
        else:
            self.queue.popleft()

    def getmax(self):
        return self.queue[0][0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monoqueue = MonoQueue()
        i = 0
        while i < k - 1:
            monoqueue.push(nums[i])
            i += 1
        res = []
        while i < len(nums):
            monoqueue.push(nums[i])
            res.append(monoqueue.getmax())
            monoqueue.pop()
            i += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))