"""
still use sort, but with auxiliary space to make the code more readable
"""


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numscopy = sorted(nums)[::-1]
        for i in range(len(nums)):
            nums[(2*i+1) % (len(nums) | 1)] = numscopy[i]

if __name__ == "__main__":
    # nums = [1,5,1,1,6,4]
    # nums = [1, 3, 2, 2, 3, 1]
    # nums = [1]
    nums = [5, 3, 1, 2, 6, 7, 8, 5, 5]
    sol = Solution()
    sol.wiggleSort(nums)
    print(nums)