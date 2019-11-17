class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i = 0
      for num in nums:
        if i < 2 or num > nums[i-2]:
          nums[i] = num
          i += 1
      return i

    # extend to k
    def removeKduplicates(self, nums, k):
      i = 0
      for num in nums:
        if i < k or num > nums[i-k]:
          nums[i] = num
          i += 1
      return i