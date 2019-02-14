"""
time complexity O(n)
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        idx = len(nums)
        # find the first index i, that nums[i] < nums[i+1]
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
        if idx == len(nums):
            nums.reverse()
            return
        # start from the end, finds first index j, so that nums[j] > nums[i]
        # because nums[i+1:] are sorted in descending order, so start from end can ensure
        # the first j that nums[j] > nums[i] is the closes value to nums[i]
        nextidx = len(nums)-1
        while nextidx > idx:
            if nums[nextidx] > nums[idx]:
                break
            nextidx -= 1
        nums[idx], nums[nextidx] = nums[nextidx], nums[idx]
        # reverse nums[i+1:]
        i, j = idx+1, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    # nums = [2, 3, 1, 3, 3]
    nums = [1,5,1]
    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)
