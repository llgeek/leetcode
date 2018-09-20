#retry the solution


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def nonzeroIndex(grid):
            for i, row in enumerate(grid):
                for j, ele in enumerate(row):
                    if ele == '1':
                        return (i, j)
            return (-1,-1)
        def exploregrid(grid, idx):
            x, y = idx[0], idx[1]
            leftidx, rightidx = idx[0]-1, idx[0]+1
            upidx, downidx = idx[1] -1, idx[1] + 1
            grid[x][y] = "0"
            if leftidx >=0 and grid[leftidx][y] == '1':
                exploregrid(grid, (leftidx, y))
            if rightidx < len(grid) and grid[rightidx][y] == '1':
                exploregrid(grid, (rightidx, y))
            if upidx >= 0 and grid[x][upidx] == '1':
                exploregrid(grid, (x, upidx))
            if downidx < len(grid[0]) and grid[x][downidx] == '1':
                exploregrid(grid, (x, downidx))
        if not grid or not grid[0]:
            return 0
        tmpgrids = grid.copy()
        res = 0
        nonzeroidx = nonzeroIndex(tmpgrids)
        while nonzeroidx[0] != -1:
            exploregrid(tmpgrids, nonzeroidx)
            res += 1
            nonzeroidx = nonzeroIndex(tmpgrids)
        return res
            

if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], [
    "0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(Solution().numIslands(grid))
