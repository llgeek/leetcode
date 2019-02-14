"""
general method for N sum problem

time complexity for N sum: O(n^(N-1)), n is the length of array nums
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        
        def NSum(l, r, target, N, result):
            if r-l+1 < N or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:
                while l < r:
                    tmps = nums[l] + nums[r]
                    if tmps == target:
                        ans.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                    elif tmps < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        NSum(i+1, r, target-nums[i], N-1, result + [nums[i]])
        
        NSum(0, len(nums)-1, target, 4, [])
        return ans 
    

if __name__ == "__main__":
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    nums = [-1, 2, 2, -5, 0, -1, 4]
    target = 3
    sol = Solution()
    print(sol.fourSum(nums, target))

