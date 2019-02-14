"""
use dict to store(key, time)
use a minheap to store (key, modifiedtime)
when replace happens, keep pop minheap out, until we find for the poped key,
the modifiedtime corresponds to the time stred in dict, that's the valid modified time
"""


import heapq
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.timer = 0
        self.userecord = dict()
        self.historyheap = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.timer += 1
        self.userecord[key] = self.timer
        heapq.heappush(self.historyheap, (self.timer, key))
        return self.cache[key]

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.timer += 1
        if key not in self.cache and len(self.cache) == self.capacity:
            while self.historyheap[0][1] not in self.userecord or self.historyheap[0][0] != self.userecord[self.historyheap[0][1]]:
                heapq.heappop(self.historyheap)
            lrukey = heapq.heappop(self.historyheap)[1]
            self.userecord.pop(lrukey, 0)
            self.cache.pop(lrukey, 0)            
        self.cache[key] = value
        self.userecord[key] = self.timer
        heapq.heappush(self.historyheap, (self.timer, key))
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
