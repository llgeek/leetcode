from collections import deque
class Solution(object):
    def __init__(self, arrays):
        self.queue = deque()
        self.arrays = arrays[:]
        for idx, array in enumerate(arrays):
            self.queue.append((idx, 0, len(array)-1))

    def next(self):
        while self.hasNext():
            idx, curptr, end = self.queue.popleft()
            if curptr > end:
                continue
            if curptr < end:
                self.queue.append((idx, curptr+1, end))
            return self.arrays[idx][curptr]
        return None

    def hasNext(self):
        return True if self.queue else False


arrays = [[1,2], [3,4,5,6], [8,9]]
s = Solution(arrays)
while s.hasNext():
    print(s.next())