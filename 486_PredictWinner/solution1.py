class Solution:
"""
Recursion
consider all cases
"""
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.minimaxgame(nums, 0, len(nums)-1, 1) >= 0

    def minimaxgame(self, nums, sidx, eidx, turn):
        """
        turn: 1 represents player 1, -1 represents player 2

        rtype: int, player1's score - player2's score
        """
        if sidx == eidx:
            return turn * nums[sidx]
        left = turn * nums[sidx] + self.minimaxgame(nums, sidx+1, eidx, -1*turn)
        right = turn * nums[eidx] + self.minimaxgame(nums, sidx, eidx-1, -1*turn)
        return turn*max(turn*left, turn*right)

