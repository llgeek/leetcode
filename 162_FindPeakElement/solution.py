"""
very nice binary search idea

see https://leetcode.com/problems/find-peak-element/solution/ for illustration

note nums[i] != nums[i+1]

O(log n) time complexity
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            if left == right:
                return left
            mid  = (left + right) >> 1
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        


