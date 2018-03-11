import random
class Solution:
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.pick(target)
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.rnd = random
        self.count = 0
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        self.rnd.seed()
        self.count = 0
        ridx = -1
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue
            self.count += 1
            if self.rnd.randint(1, self.count) == self.count:
                ridx = i
        return ridx



    

        


