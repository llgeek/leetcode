class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, m, n, visited):
            ans = 0
            visited.add((i, j))
            for nebx, neby in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                nebi, nebj = i + nebx, j + neby
                if 0 <= nebi < m and 0 <= nebj < n and grid[nebi][nebj] and (nebi, nebj) not in visited:
                    ans = max(ans, dfs(nebi, nebj, m, n, visited))
            visited.discard((i, j))
            return ans + grid[i][j]

        if not grid or not any(grid):
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j, m, n, set()))
        return ans
