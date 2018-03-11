"""
memorization
"""

# class Solution:
#     def PredictTheWinner(self, nums):
#         self.scorememo = [[None for _ in range(len(nums))] for __ in range(len(nums))]
#         self.winner(nums, 0, len(nums)-1)
#         return self.scorememo[0][len(nums)-1] >= 0

#     def winner(self, nums, sidx, eidx):
#         if sidx == eidx:
#             return nums[sidx]
#         if self.scorememo[sidx][eidx] != None:
#             return self.scorememo[sidx][eidx]
#         self.winner(nums, sidx+1, eidx)
#         self.winner(nums, sidx, eidx-1)
#         left = nums[sidx] - self.scorememo[sidx+1][eidx]
#         right = nums[eidx] - self.scorememo[sidx][eidx-1]
#         self.scorememo[sidx][eidx] =  max(left, right)
#
class Solution:
    def PredictTheWinner(self, nums):
        self.scorememo = [[None for _ in range(len(nums))] for __ in range(len(nums))]
        return self.winner(nums, 0, len(nums)-1) >= 0

    def winner(self, nums, sidx, eidx):
        if sidx == eidx:
            return nums[sidx]
        if self.scorememo[sidx][eidx] != None:
            return self.scorememo[sidx][eidx]
        left = nums[sidx] - self.winner(nums, sidx+1, eidx)
        right = nums[eidx] - self.winner(nums, sidx, eidx-1)
        self.scorememo[sidx][eidx] =  max(left, right)
        return self.scorememo[sidx][eidx]


s = Solution()
num = [1, 5, 233, 7]
print(s.PredictTheWinner(num))

