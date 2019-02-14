"""
naive way, sort the array

O(nlgn) time complexity

after sort, put 
"""


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums[::2])-1
        nums[::2], nums[1::2] = nums[n::-1], nums[:n:-1]


if __name__ == "__main__":
    nums = [1, 5, 1, 1, 6, 4]
    sol = Solution()
    sol.wiggleSort(nums)
    print(nums)
