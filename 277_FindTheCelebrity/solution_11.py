

class Solution:
    def knows(self, a, b):
        pass
    
    def findCelebrity(self, n):
        res = 0
        for i in range(1, n):
            if self.knows(res, i):
                res = i
        for j in range(n):
            if j != res and (not self.knows(j, res) or self.knows(res, j)):
                return -1
        return res