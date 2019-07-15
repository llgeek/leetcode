from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre, cur = -1, 0
        while cur < len(nums):
            if nums[cur] != 0:
                if pre != -1:
                    nums[pre], nums[cur] = nums[cur], nums[pre]
                    pre += 1
            else:
                if pre == -1:
                    pre = cur    
            cur += 1
