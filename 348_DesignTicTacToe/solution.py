class Solution:
    def tic_tac_toe(self, n):
        def __init__(self, n):
            self.row = [0] * n
            self.col = [0] * n
            self.diag = self.rev_diag = 0

        def move(self, row, col, player):
            val = 1 if player == 1 else -1
            self.row[row] += val
            self.col[col] += val
            self.diag += val if row == col else 0
            self.rev_diag += val if row + col == N - 1 else 0
            return player if abs(self.row[row]) == N or abs(self.col[col]) == N or \ 
                abs(self.diag) == N or abs(self.rev_diag) == N else 0
