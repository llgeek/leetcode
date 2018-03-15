class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def DFSMarking(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            DFSMarking(i+1, j)
            DFSMarking(i-1, j)
            DFSMarking(i, j+1)
            DFSMarking(i, j-1)
        
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    DFSMarking(i, j)
                    count += 1
        return count


grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
print(Solution().numIslands(grid))
