"""
time complexity: O(n^3)
"""



class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def threesum(nums, target):
            if not nums or len(nums) < 3:
                return []
            if nums[0] + nums[1] + nums[2] > target or nums[-1] + nums[-2] + nums[-3] < target:
                return []
            i = 0
            res = []
            while i < len(nums) - 2:
                if i == 0 or nums[i] != nums[i-1]:
                    lo = i + 1
                    hi = len(nums)-1
                    remain = target - nums[i]
                    while lo < hi:
                        cursum = nums[lo] + nums[hi]
                        if cursum == remain:
                            res.append([nums[i], nums[lo], nums[hi]])
                            while lo < hi and nums[lo] == nums[lo+1]:
                                lo += 1
                            lo += 1
                            while lo < hi and nums[hi] == nums[hi-1]:
                                hi -= 1
                            hi -= 1
                        elif cursum < remain:
                            lo += 1
                        else:
                            hi -= 1
                i += 1
            return res

        nums = sorted(nums)
        i = 0
        res = []
        while i < len(nums)-3:
            if i == 0 or nums[i] != nums[i-1]:
                tmpres = threesum(nums[i+1:], target-nums[i])
                if tmpres:
                    for tmptrip in tmpres:
                        res.append([nums[i]] + tmptrip)
            i += 1
        return res


if __name__ == "__main__":
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    nums = [-1, 2, 2, -5, 0, -1, 4]
    target = 3
    sol = Solution()
    print(sol.fourSum(nums, target))
