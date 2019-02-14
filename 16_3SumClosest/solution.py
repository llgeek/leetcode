"""
time complexity: O(n^2)
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        nums = sorted(nums)
        res = (1 << 31) - 1
        diff = (1 << 31) - 1
        i = 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i-1]:
                lo = i + 1
                hi = len(nums) - 1
                remain = target - nums[i]
                while lo < hi:
                    tmpsum = nums[lo] + nums[hi] + nums[i]
                    if tmpsum == target:
                        return target
                    if abs(nums[lo] + nums[hi] -remain) < diff:
                        diff = abs(nums[lo] + nums[hi] - remain)
                        res = nums[i] + nums[lo] + nums[hi]
                        # while lo < hi and nums[lo] == nums[lo+1]:
                        #     lo += 1
                        # lo += 1
                        # while hi > lo and nums[hi] == nums[hi-1]:
                        #     hi -= 1
                        # hi -= 1
                    if tmpsum > target:
                        hi -= 1
                    if tmpsum < target:
                        lo += 1
            i += 1
        return res

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))
    
