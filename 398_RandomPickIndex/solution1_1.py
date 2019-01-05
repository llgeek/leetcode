"""
re-write the solution
"""
import random

class Solution:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                rnd = random.randint(0, cnt)
                res = i if not rnd else res
                cnt += 1
        return res

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)