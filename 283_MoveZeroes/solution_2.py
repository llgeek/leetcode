from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroid, nonzeroid = 0, 0
        while nonzeroid < len(nums):
          if nums[nonzeroid] != 0:
            nums[zeroid], nums[nonzeroid] = nums[nonzeroid], nums[zeroid]
            zeroid += 1
          nonzeroid += 1
