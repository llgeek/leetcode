
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      dp = {num: 1 for num in nums}
      for i in range(len(nums)):
        for j in range(i):
          if nums[j] < nums[i]:
            dp[nums[i]] = max(dp[nums[i]], dp[nums[j]]+1)
      return max(dp.values())
