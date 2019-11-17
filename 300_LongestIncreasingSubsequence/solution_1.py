"""
LTE
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
          dp[i][i] = 1
        for l in range(2, len(nums)+1):
          for i in range(len(nums)):
            j = i + l - 1
            if j >= len(nums): break
            for k in range(i, j+1):
              if nums[k] < nums[j]:
                dp[i][j] = max(dp[i][j], dp[i][k] + 1)
        return max(dp[i][j] for i in range(len(nums)) for j in range(i, len(nums)))

if __name__ == "__main__":
    sol = Solution()
    # nums = [10,9,2,5,3,7,101,18]
    nums = [-2, -1]
    print(sol.lengthOfLIS(nums))
