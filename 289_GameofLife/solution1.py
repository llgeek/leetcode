"""
naive solution, store previous state, computed state stored in another place
"""

class Solution:
    def gameOfLife(self, board):
        def ifLiveNext(idx, idy):
            liveneb, deadneb = 0, 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0: continue
                    nidx, nidy = idx+i, idy+j
                    if nidx >= 0 and nidx < m and nidy >= 0 and nidy < n:
                        if board[nidx][nidy]:
                            liveneb += 1
                        else:
                            deadneb += 1
            if board[idx][idy]:
                if liveneb < 2:
                    return 0
                if liveneb == 2 or liveneb == 3:
                    return 1
                if liveneb > 3:
                    return 0
            else:
                if liveneb == 3:
                    return 1
                else:
                    return 0

        if not board:
            return
        m, n = len(board), len(board[0])
        newboard = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                newboard[i][j] = ifLiveNext(i, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = newboard[i][j]

s = Solution()
# b = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
b = [[1,1]]
print(b)
print()
s.gameOfLife(b)
print(b)