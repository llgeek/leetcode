from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2], nums[1::2] = nums[len(nums[::2])-1::-1], nums[:len(nums[::2])-1:-1]
        