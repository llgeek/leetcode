class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, startidx, result):
            if startidx >= len(nums):
                return
            tmpresult = result[:]
            for tmpr in tmpresult:
                tmpr = tmpr[:]
                tmpr.append(nums[startidx])
                result.append(tmpr)
            helper(nums, startidx+1, result)

        if not nums:
            return []
        result = [[]]
        helper(nums, 0, result)
        return result
    
nums = [1,2,3]
print(Solution().subsets(nums))
