"""
带时间戳的map: put(k, v, timestamp) get(k , timestamp)EX:
put(1, haha , 3) put(1, ha, 5) get(1, 0) -> null get(1, 4) -> haha get(1, 6) -> ha
Follow Up: ArrayList, LinkedList, BST, balancedBST 分别get & put 时间复杂度

Page 1
"""
import bisect

class Solution:
    def __init__(self):
        self._timemap = dict()

    def put(self, key, value, timestamp):
        if key in self._timemap:
            #bisect.insort_right(self._timemap[key], (value, timestamp))
            self._timemap[key].append((value, timestamp))
            self._timemap[key].sort(key = lambda x: x[1])
        else:
            self._timemap[key] = [(value, timestamp)]


    def get(self, key, timestamp):
        if key not in self._timemap:
            return None
        i = len(self._timemap[key]) - 1
        while i >= 0 and self._timemap[key][i][1] > timestamp:
            i -= 1
        if i < 0:
            return None
        else:
            return self._timemap[key][i][0]

s = Solution()
s.put(1, 'haha', 3)
s.put(1, 'ha', 5)
print(s.get(1, 0))
print(s.get(1,4))
print(s.get(1, 6))
            
