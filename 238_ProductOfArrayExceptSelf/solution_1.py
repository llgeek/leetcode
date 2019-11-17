class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromleft = [1 for _ in range(len(nums))]
        fromright = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
          fromleft[i] = fromleft[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
          fromright[i] = fromright[i+1] * nums[i+1]
        res = [fromleft[i] * fromright[i] for i in range(len(nums))]