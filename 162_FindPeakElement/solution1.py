"""
linear scan idea

O(n) time complexity

only need to compare with the right element, 
no need for comparision with left element
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx in range(len(nums)-1):
            if nums[idx] > nums[idx+1]:
                return idx
        return len(nums)-1
