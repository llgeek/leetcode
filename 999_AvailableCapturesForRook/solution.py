class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def findrookidx(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 'R':
                        return (i, j)
            return (-1, -1)

        x, y = findrookidx(board)
        res = 0
        if x > 0:
            newx, newy = x-1, y
            while newx > 0 and board[newx][newy] == '.':
                newx -= 1
            res += int(board[newx][newy] == 'p')
        if x < len(board)-1:
            newx, newy = x+1, y
            while newx < len(board)-1 and board[newx][newy] == '.':
                newx += 1
            res += int(board[newx][newy] == 'p')
        if y > 0:
            newx, newy = x, y-1
            while newy > 0 and board[newx][newy] == '.':
                newy -= 1
            res += int(board[newx][newy] == 'p')
        if y < len(board[0])-1:
            newx, newy = x, y+1
            while newy < len(board[0])-1 and board[newx][newy] == '.':
                newy += 1
            res += int(board[newx][newy] == 'p')
        return res
