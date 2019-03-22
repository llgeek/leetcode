"""
backtracker
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m, n):
            if m == 1 or n == 1:
                self.memo[1, max(m,n)] = 1
                return 1
            if (min(m,n), max(m, n)) not in self.memo:
                self.memo[(min(m, n), max(m, n))] = helper(
                    m-1, n) + helper(m, n-1)
            return self.memo[(min(m, n), max(m, n))]

        self.memo = {}
        return helper(m, n)
        

if __name__ == "__main__":
    m = 23
    n = 12
    sol = Solution()
    print(sol.uniquePaths(m, n))
