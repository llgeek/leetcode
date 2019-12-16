from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.Y = set()
        self.NE = set()
        self.NW = set()
        self.state = set()
        def backtracker(row):
            if row == n:
                placeboard()
                return
            for col in range(n):
                if col not in self.Y and row - col not in self.NE and row + col not in self.NW:
                    self.Y.add(col)
                    self.NE.add(row - col)
                    self.NW.add(row + col)
                    self.state.add((row, col))
                    backtracker(row+1)
                    self.Y.discard(col)
                    self.NE.discard(row - col)
                    self.NW.discard(row + col)
                    self.state.discard((row, col))

        def placeboard():
            board = [['.' for _ in range(n)] for _ in range(n)]
            for i, j in self.state:
                board[i][j] = 'Q'
            self.res.append(["".join(row) for row in board])
        
        backtracker(0)
        return self.res

if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.solveNQueens(n))