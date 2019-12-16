class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == '.': continue
                if str(val) + 'in row ' + str(i) in seen:
                    return False
                seen.add(str(val) + 'in row ' + str(i))
                if str(val) + 'in column ' + str(j) in seen:
                    return False
                seen.add(str(val) + 'in column ' + str(j))
                if str(val) + 'in grid ' + str(i // 3) + ' ' + str(j // 3) in seen:
                    return False
                seen.add(str(val) + 'in grid ' + str(i // 3) + ' ' + str(j // 3))
        return True