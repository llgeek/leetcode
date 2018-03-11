class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i = len(nums)-2
        prenum = nums[-1]
        while i >= 0:
            if nums[i] < prenum:
                break
            prenum = nums[i]
            i -= 1
        if i < 0:
            nums.reverse()
            return
        j = len(nums)-1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        j = len(nums)-1
        i += 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
solution = Solution()
nums = [1,5,1]
solution.nextPermutation(nums)
print(nums)

        
