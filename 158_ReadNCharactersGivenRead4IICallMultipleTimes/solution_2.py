class Solution(object):
    def __init__(self):
        self.cache = [None] * 4
        self.cachesize = 0
        self.idx = 0

    def solution(self, buff, n):
        readnum = 0
        while self.idx < self.cachesize and readnum < n:
            buff[readnum] = self.cache[self.idx]
            self.idx += 1
        if self.idx == self.cachesize:
            self.idx = 0
            self.cachesize = 0
            self.cache = [None] * 4
        while readnum < n:
            self.cachesize = read4(self.cache)
            while self.idx < self.cachesize:
                buff[readnum] = self.cache[self.idx]
                self.idx += 1
                readnum += 1
                if readnum == n:
                    break
            if self.cachesize < 4:
                break
        return readnum




