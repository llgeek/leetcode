class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        initcnt = dict(zip(range(1, 10), [0]*9))
        initcnt = {str(k): v for k, v in initcnt.items()}
        def rowcheck():
            for i in range(len(board)):
                cnt = initcnt.copy()
                for val in board[i]:
                    if val == '.': continue
                    cnt[val] += 1
                    if cnt[val] > 1:
                        return False
            return True
        def columncheck():
            for j in range(len(board[0])):
                cnt = initcnt.copy()
                for i in range(len(board)):
                    if board[i][j] == '.': continue
                    cnt[board[i][j]] += 1
                    if cnt[board[i][j]] > 1:
                        return False
            return True
        def gridcheck():
            for i in range(0, len(board), 3):
                for j in range(0, len(board[0]), 3):
                    cnt = initcnt.copy()
                    for ii in range(i, i+3):
                        for jj in range(j, j+3):
                            if board[ii][jj] == '.': continue
                            cnt[board[ii][jj]] += 1
                            if cnt[board[ii][jj]] > 1:
                                return False
            return True
        return rowcheck() and columncheck() and gridcheck()