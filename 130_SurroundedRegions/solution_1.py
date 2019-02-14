"""
second trial

DFS based solution
"""

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def DFS(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = '0'
            for d in distance:
                DFS(x+d[0], y+d[1]) 

        
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        distance = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for j in range(n):
            if board[0][j] == 'O':
                DFS(0, j)
            if m -1 != 0 and board[m-1][j] == 'O':
                DFS(m-1, j)
        for i in range(1,m-1):
            if board[i][0] == 'O':
                DFS(i, 0)
            if n-1 != 0 and board[i][n-1] == 'O':
                DFS(i, n-1)
        # list(map(lambda x, y: board[x][y] = 'X' if board[x][y] == 'O' else board[x][y], range(m), range(n)))
        # list(map(lambda x, y: board[x][y]='O' if board[x][y] == '0' else board[x][y], range(m), range(n)))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '0':
                    board[i][j] = 'O'


        


