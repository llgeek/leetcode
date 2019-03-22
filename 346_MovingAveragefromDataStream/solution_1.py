from collections import deque
class Solution:
    def __init__(self, winlen):
        self.winlen = winlen
        self.avg = 0
        self.queue = deque()

    def next(self, num):
        if len(self.queue) < self.winlen:
            self.avg = (self.avg * len(self.queue) + num) / len((self.queue) + 1)
            self.queue.append(num)
        else:
            self.avg = (self.avg * len(self.queue) - self.queue[0] + num) / len(self.queue)
            self.queue.popleft()
            self.queue.append(num)
        return self.avg

            
