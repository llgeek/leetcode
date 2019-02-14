"""
second trial

DFS based
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def searchOne(m, n):
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1':
                        return (i, j)
            return (-1, -1)

        def DFS(xid, yid, m, n):
            if xid < 0 or xid >= m or yid < 0 or yid >= n or grid[xid][yid] == '0':
                return
            grid[xid][yid] = "0"
            for d in distance:
                DFS(xid+d[0], yid+d[1], m, n)

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        distance = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        xid, yid = searchOne(m, n)
        ret = 0
        while xid != -1 and yid != -1:
            ret += 1
            DFS(xid, yid, m, n)
            xid, yid = searchOne(m, n)
        return ret

