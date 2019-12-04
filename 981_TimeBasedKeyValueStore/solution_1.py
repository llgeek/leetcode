from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key] += [(timestamp, value)]
    
    def helper(self, array, start, end, target):
      while start <= end:
        mid = start + (end - start) // 2
        if array[mid][0] > target:
          end = mid - 1
        else:
          start = mid + 1
        return end

    def get(self, key: str, timestamp: int) -> str:
      if key not in self.dict:
        return ""
      else:
        idx = self.helper(self.dict[key], 0, len(self.dict[key])-1, timestamp)
        if idx == -1:
          return ""
        else:
          return self.dict[key][idx][1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)