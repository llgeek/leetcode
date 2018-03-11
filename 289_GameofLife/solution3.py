"""
solution for the case when the board is infinite
"""
import collections

class Solution:
    def gameOfLife(self, board):
        """
        here we assume the board can be infinite, which cannot be represented in a 2-dimensonal list
        """
        if not board:
            return 
        livespot = {(idx, idy) for idx, row in enumerate(board) for idy, live in enumerate(row) if live}
        livespot = self.gameOfLifeInfinite(livespot)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = int((i, j) in livespot)


    def gameOfLifeInfinite(self, livespot):
        ctr = collections.Counter((nidx, nidy)
            for idx, idy in livespot
                for nidx in range(idx-1, idx+2)
                    for nidy in range(idy-1, idy+2)
                    if nidx != idx or nidy != idy)
        return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in livespot}

s = Solution()
b = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
#b = [[1,1]]
print(b)
print()
s.gameOfLife(b)
print(b)
