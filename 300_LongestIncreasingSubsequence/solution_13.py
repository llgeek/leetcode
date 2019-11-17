"""
BST
optimize to O(nlogn)
"""

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      
      def bst(start, end, val):
        while start <= end:
          mid = start + (end - start) // 2
          if sortednums[mid] >= val:
            end = mid - 1
          else:
            start = mid + 1
        return end
      
      if not nums: return 0
      sortednums = [0] * len(nums)
      length = 1
      sortednums[0] = nums[0]
      for i in range(1, len(nums)):
        idx = bst(0, length-1, nums[i])
        if idx == length-1:
          length += 1
        sortednums[idx+1] = nums[i]
      return length
      
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,6,7,9,4,10,5,6]
    print(sol.lengthOfLIS(nums))