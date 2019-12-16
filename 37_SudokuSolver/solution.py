"""
wrong ans
"""
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board) or len(board) != 9 or len(board[0]) != 9:
            return
        self.solver(board)

    def solver(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        c = str(c)
                        if self.valid(board, i, j, c):
                            board[i][j] = c
                            if self.solver(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True



    def valid(self, board, row, col, c):
        for i in range(len(board)):
            if board[i][col] == c:
                return False
        for j in range(len(board[0])):
            if board[row][j] == c:
                return False
        for i in range(row // 3 * 3, row // 3 * 3 + 3):
            for j in range(col // 3 * 3, col // 3 * 3 + 1):
                if board[i][j] == c:
                    return False
        return True
        

if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board)
    print(board)
    # board = [["5","3","1","6","7","8","9","2","4"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","7","5","6","2"],["8","1","9","7","6","2","4","5","3"],["4","2","6","8","5","3","7","9","1"],["7","5","3","9","2","4","8","1","6"],["9","6","4","5","3","1","2","8","7"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         c = board[i][j]
    #         board[i][j] = '.'
    #         if not sol.valid(board, i, j, c):
    #             print(i, j, c)
    #             print('falid')
    #         board[i][j] = c