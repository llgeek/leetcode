

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pre, cur = 0, 1
        while cur < len(nums):
            while cur < len(nums) and nums[pre] == nums[cur]:
                cur += 1
            if cur < len(nums):
                nums[pre+1], nums[cur] = nums[cur], nums[pre+1]
                pre += 1
                cur += 1
        return pre+1

        
