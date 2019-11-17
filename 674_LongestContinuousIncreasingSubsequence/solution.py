from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        for i in range(len(nums)-1, 0, -1):
          nums[i] -= nums[i-1]
        left, right = 0, 1
        res = 1
        while right < len(nums):
          if nums[right] <= 0:
            res = max(res, right-left)
            left = right
          right += 1
        return max(res, right-left)