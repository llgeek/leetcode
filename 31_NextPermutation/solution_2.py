"""
third trial
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i != -1:
            j = len(nums)-1
            while i < j:
                if nums[j] > nums[i]:
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        s, e = i + 1, len(nums)-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

if __name__ == "__main__":
    # nums = [1,2,3]
    nums = [5,1,1]
    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)


