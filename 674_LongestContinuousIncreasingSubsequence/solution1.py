from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
      res, cnt = 0, 0
      for i in range(len(nums)):
        if i == 0 or nums[i] > nums[i-1]: 
          cnt += 1
        else:
          res = max(res, cnt)
          cnt = 1
      return max(res, cnt)