class Solution(object):
    def __init__(self):
        self.res = 0
        self.X = set()
        self.leftdiag = set()
        self.rightdiag = set()
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(rownum, n):
            if rownum == n:
                self.res += 1
                return
            for i in range(n):
                if i not in self.X and (i-rownum) not in self.leftdiag and i+rownum not in self.rightdiag:
                    self.X.add(i)
                    self.leftdiag.add(i-rownum)
                    self.rightdiag.add(i+rownum)
                    backtrack(rownum+1, n)
                    self.X.discard(i)
                    self.leftdiag.discard(i-rownum)
                    self.rightdiag.discard(i+rownum)
        if n==0:
            return 0
        backtrack(0, n)
        return self.res

if __name__ == "__main__":
    n = 0
    sol = Solution()
    print(sol.totalNQueens(n))
