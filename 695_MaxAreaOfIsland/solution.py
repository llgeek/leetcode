from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.accarea = 0
        if not any(grid): return 0
        def helper(i, j):
            self.accarea += 1
            grid[i][j] = -1
            for ni, nj in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                ni += i
                nj += j
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    helper(ni, nj)
            

        def findone():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return i, j
            return -1, -1
        
        i, j = findone()
        res = 0
        while i != -1:
            helper(i, j)
            res = max(res, self.accarea)
            self.accarea = 0
            i, j = findone()
        return res

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,1],[1,0]]
    print(sol.maxAreaOfIsland(grid))