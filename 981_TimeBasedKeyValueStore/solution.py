# write own binary search, or
# use internal bisect module

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyval = dict()
        # self.
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyval:
            self.keyval[key] = [(timestamp, value)]
        else:
            self.keyval[key].append((timestamp, value))
        
    
    def bisearch(self, vallist, target):
        if not vallist: return -1
        if target < vallist[0][0]: return -1
        if target >= vallist[-1][0]: return len(vallist)-1
        start, end = 0, len(vallist)-1
        while start < end:
            mid = (start + end+1) // 2  ## IMPORTANT!! use ceil instead of floor, to avoid dead loop
            if vallist[mid][0] <= target:
                start = mid
            else:
                end = mid-1
        return start

    def get(self, key: str, timestamp: int) -> str:
        idx = self.bisearch(self.keyval.get(key, []), timestamp)
        if idx != -1:
            return self.keyval[key][idx][1]
        else:
            return ''

    def get_v2(self, key:str, timestamp: int) -> str:
        import bisect
        idx = bisect.bisect(self.keyval.get(key, None), (timestamp, chr(127)))
        if idx != -1:
            return self.keyval[key][idx-1][1]
        else:
            return ''


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)