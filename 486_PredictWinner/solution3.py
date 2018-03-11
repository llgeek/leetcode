"""
dynamic programming
"""

class Solution:
    def PredictTheWinner(self, nums):
        self.scorememo = [[None for _ in range(len(nums))] for __ in range(len(nums))]
        self.winner(nums)
        return self.scorememo[0][len(nums)-1] >= 0

    def winner(self, nums):
        for idx in range(len(nums)):
            for i in range(len(nums)-idx):
                j = i+idx
                if i == j:
                    self.scorememo[i][j] = nums[i]
                else:
                    left = nums[i] - self.scorememo[i+1][j]
                    right = nums[j] - self.scorememo[i][j-1]
                    self.scorememo[i][j] = max(left, right)


s = Solution()
num = [1, 5, 233, 7]
print(s.PredictTheWinner(num))
