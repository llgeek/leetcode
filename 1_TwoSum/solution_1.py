class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seeval = dict()
        for idx, val in enumerate(nums):
            if target - val in seeval:
                return [seeval[target - val], idx]
            seeval[val] = idx
        return [-1,-1]        
