"""
improve the complexity to O(n)

just one single traversal

when index i is odd, make sure nums[i-1] >= nums[i]
when index i is even, make sure nums[i-1] <= nums[i]
"""

class Solution:
    def wiggleSort(self, nums):
        for idx in range(1, len(nums)):
            if (idx % 2 == 0 and nums[idx-1] < nums[idx]) or (idx % 2 and nums[idx-1] > nums[idx]):
                nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
            

if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 4]
    sol = Solution()
    sol.wiggleSort(nums)
    print(nums)

