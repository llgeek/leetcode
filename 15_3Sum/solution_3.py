"""
extend to k-sum
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums = sorted(nums)
      i = 0
      res = []
      while i < len(nums):
        if nums[i] * 3 > 0: break
        j = i + 1
        k = len(nums) - 1
        while j < k:
          if nums[j] + nums[k] + nums[i] == 0:
            res.append([nums[i], nums[j], nums[k]])
            while k - 1 > j and nums[k] == nums[k-1]:
              k -= 1
            k -= 1
            while j + 1 < k and nums[j] == nums[j+1]:
              j += 1
            j += 1
          elif nums[j] + nums[k] + nums[i] > 0:
            while k - 1 > j and nums[k] == nums[k-1]:
              k -= 1
            k -= 1
          elif nums[j] + nums[k] + nums[i] < 0:
            while j + 1 < k and nums[j] == nums[j+1]:
              j += 1
            j += 1
        while i + 1< len(nums) and nums[i] == nums[i+1]:
          i += 1
        i += 1
      return res
          
        