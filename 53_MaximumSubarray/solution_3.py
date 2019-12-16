class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
        