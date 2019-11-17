class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        res = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
          dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]
          res = max(res, dp[i])
        return res