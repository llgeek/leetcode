import heapq
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.usedtime = dict()
        self.usedtimeheap = []
        self.time = -1


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.time += 1
        heapq.heappush(self.usedtimeheap, (self.time, key))
        self.usedtime[key] = self.time
        return self.cache[key]
        


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.time += 1
        if key in self.cache:
            self.cache[key] = value
            self.usedtime[key] = self.time
            heapq.heappush(self.usedtimeheap, (self.time, key))
        if len(self.cache) == self.capacity:
            t, k = heapq.heappop(self.usedtimeheap)
            while k not in self.usedtime or t != self.usedtime[k]:
                t, k = heapq.heappop(self.usedtimeheap)
            self.cache.pop(k, 0)
            self.usedtime.pop(k, 0)
        
        self.cache[key] = value
        self.usedtime[key] = self.time
        heapq.heappush(self.usedtimeheap, (self.time, key))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
