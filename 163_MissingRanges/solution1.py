class Solution:
    # Too verbose, rewrite in solution1.py
    # because there is one assumption that nums always in range [lower, upper]!
    # This solution won't pass the test case, when upper = INT_MAX!!!
    def missingRanges(self, nums, lower, upper):
        """  
        type nums: list of sorted intergers
        type lower: int, lower range
        type upper: int, upper range
        rtype: list of missing ranges
        """
        prenum, curnum = lower-1, 0
        result = []
        for i in range(len(nums)+1):
            curnum = upper + 1 if i == len(nums) else nums[i]
            if curnum - prenum >= 2:
                if curnum - prenum == 2:
                    result.append(str(prenum + 1))
                else:
                    result.append('{}->{}'.format(prenum + 1, curnum - 1))
            prenum = curnum 
        return result
            

nums = [0, 1, 3, 50, 75, 100]
print(Solution().missingRanges(nums, 0, 99))
        
