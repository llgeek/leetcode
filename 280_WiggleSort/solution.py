"""
simpliest way to do it is firstly sort the array,
the swap the 2th and 3th, 4th and 5th, ...

time complexity: O(nlgn)
"""


class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        idx = 1
        while idx < len(nums) and idx + 1 < len(nums):
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            idx += 2


if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 4]
    sol = Solution()
    sol.wiggleSort(nums)
    print(nums)
