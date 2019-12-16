class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos0, pos1, pos2 = 0, 0, len(nums)-1
        while pos1 <= pos2:
            if nums[pos1] == 1:
                pos1 += 1
            elif nums[pos1] == 0:
                nums[pos0], nums[pos1] = nums[pos1], nums[pos0]
                pos0 += 1
                pos1 += 1
            else:
                nums[pos2], nums[pos1] = nums[pos1], nums[pos2]
                pos2 -= 1
