"""
sorted based 

key point is to find three largest numbers, and two smallest numbers

time complexity: O(nlgn)
"""

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = nums[0]*nums[1]*nums[-1]
        right = nums[-1]*nums[-2]*nums[-3]
        return max(left, right)
