"""
second trial

union-find based solution
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        UF = UnionFind(grid)
        distance = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in distance:
                        nebx, neby = i + d[0], j + d[1]
                        if 0 <= nebx < m and 0 <= neby < n and grid[nebx][neby] == '1':
                            UF.union(nebx * n + neby, i * n + j)
        return UF.cnt


class UnionFind:
    def __init__(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        self.parents = dict()
        self.cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    id = j + i * self.n
                    self.parents[id] = id
                    self.cnt += 1
        
    def union(self, p, q):
        pp = self.find(p)
        qp = self.find(q)
        if pp != qp:
            self.parents[pp] = qp
            self.cnt -= 1

    def find(self, p):
        if p == self.parents[p]:
            return p
        self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

