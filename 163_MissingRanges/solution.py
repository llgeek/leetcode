class Solution:
    # Too verbose, rewrite in solution1.py
    # because there is one assumption that nums always in range [lower, upper]!
    def missingRanges(self, nums, lower, upper):
        """  
        type nums: list of sorted intergers
        type lower: int, lower range
        type upper: int, upper range
        rtype: list of missing ranges
        """
        if not nums:
            return ['{}->{}'.format(lower, upper)]
        result = []
        for i in range(len(nums)):
            if nums[i] <= lower:
                continue 
            elif nums[i] >= upper:
                if i > 0 and nums[i-1] < upper:
                    if nums[i-1] < upper-1:
                        result.append('{}->{}'.format(nums[i-1] + 1, upper))
                    else:
                        result.append(str(upper))
                break
            elif i == 0 and nums[i] > lower:
                if nums[i] == lower + 1:
                    result.append(str(lower))
                else:
                    result.append('{}->{}'.format(lower, nums[i] - 1))
            elif i > 0 and nums[i] > nums[i-1] + 1:
                if nums[i-1] == nums[i] - 2:
                    result.append(str(nums[i-1] + 1))
                else:
                    result.append('{}->{}'.format(nums[i-1] + 1, nums[i] - 1))
        if nums[-1] < upper:
            if nums[-1] == upper - 1:
                result.append(str(upper))
            else:
                result.append('{}->{}'.format(nums[-1] + 1, upper))
        return result
    
nums = [0, 1, 3, 50, 75, 100]
print(Solution().missingRanges(nums, 0, 99))
