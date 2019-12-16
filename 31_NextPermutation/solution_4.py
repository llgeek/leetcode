from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return
        s, t = i + 1, len(nums) - 1
        while s < t:
            nums[s], nums[t] = nums[t], nums[s]
            s += 1
            t -= 1
        for k in range(i+1, len(nums)):
            if nums[k] > nums[i]:
                nums[i], nums[k] = nums[k], nums[i]
                break
                
if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1]
    sol.nextPermutation(nums)
    print(nums)