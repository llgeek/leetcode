"""
use two pass

https://leetcode.com/problems/sliding-window-maximum/discuss/65881/O(n)-solution-in-Java-with-two-simple-pass-in-the-array
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        leftmax = [0] * len(nums)
        rightmax = [0] * len(nums)
        ret = [0] * (len(nums)-k+1)
        for i in range(len(nums)):
            if i%k == 0:
                leftmax[i] = nums[i]
            else:
                leftmax[i] = max(nums[i], leftmax[i-1])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1 or (i+1) % k == 0:
                rightmax[i] = nums[i]
            else:
                rightmax[i] = max(nums[i], rightmax[i+1])
        for i in range(len(nums)-k+1):
            ret[i] = max(rightmax[i], leftmax[i+k-1])
        return ret



