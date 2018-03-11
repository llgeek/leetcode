"""
in place modify the baord solution
store the next state in second bit, first bit as the current state info
"""
class Solution:
    def gameOfLife(self, board):
        def isLiveNext(idx, idy):
            liveneb, deadneb = 0, 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0: continue
                    nidx, nidy = idx + i, idy + j
                    if nidx >= 0 and nidx < m and nidy >= 0 and nidy < n:
                        if board[nidx][nidy] & 0b01:
                            liveneb += 1
                        else:
                            deadneb += 1
            if board[idx][idy] &0b01:
                if liveneb < 2:
                    board[idx][idy] &= 0b01
                if liveneb == 2 or liveneb == 3:
                    board[idx][idy] |= 0b10
                else:
                    board[idx][idy] &= 0b01
            else:
                if liveneb == 3:
                    board[idx][idy] |= 0b10
                else:
                    board[idx][idy] &= 0b01

        if not board:
            return
        m, n = len(board), len(board[0])
        for idx in range(m):
            for idy in range(n):
                isLiveNext(idx, idy)
        for idx in range(m):
            for idy in range(n):
                board[idx][idy] >>= 1


s = Solution()
# b = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
b = [[1,1]]
print(b)
print()
s.gameOfLife(b)
print(b)