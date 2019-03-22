"""
memory limit exceeded in leetcode
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return True
        reachable = [[False] * len(nums) for _ in range(len(nums))]
        for step in range(1, len(nums)):
            for i in range(len(nums)):
                j = i + step
                if j >= len(nums):
                    continue
                if nums[i] >= step:
                    reachable[i][j] = True
                    continue
                else:
                    for k in range(step):
                        if reachable[i][k] and reachable[k][j]:
                            reachable[i][j] = True
        return reachable[0][len(nums)-1]

if __name__ == "__main__":
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    sol = Solution()
    print(sol.canJump(nums))
