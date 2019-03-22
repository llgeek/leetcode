class Solution:
    def __init__(self):
        self.state = set()
        self.Y = set()
        self.NE = set()
        self.NW = set()
        self.res = []

    def solveNQueens(self, n):
        def backtracker(n, linenum):
            if linenum == n:
                tmpres = [['.' for _ in range(n)] for _ in range(n)]
                for idx in self.state:
                    tmpres[idx[0]][idx[1]] = 'Q'
                self.res.append([''.join(line) for line in tmpres])
            else:
                for j in range(n):
                    if j not in self.Y and linenum+j not in self.NE and j-linenum not in self.NW:
                        self.Y.add(j)
                        self.NE.add(linenum+j)
                        self.NW.add(j-linenum)
                        self.state.add((linenum, j))
                        backtracker(n, linenum+1)
                        self.Y.discard(j)
                        self.NE.discard(j+linenum)
                        self.NW.discard(j-linenum)
                        self.state.discard((linenum, j))
        
        backtracker(n, 0)
        return self.res

if __name__ == "__main__":
    n = 8
    sol = Solution()
    print(sol.solveNQueens(n))