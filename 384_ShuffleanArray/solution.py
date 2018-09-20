"""
Fisher-Yates Algorithm

On each iteration of the algorithm, we generate a random integer between 
the current index and the last index of the array. Then, we swap the elements 
at the current index and the chosen index
"""



import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.defaultnums = nums.copy()
        self.nums = nums.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.defaultnums.copy()
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums)-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
