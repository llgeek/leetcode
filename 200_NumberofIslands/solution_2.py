"""
third trial

try union-find again
"""


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if not any(grid):
            return 0
        dist = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        ufhelper = UnionFind(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    for d in dist:
                        nebx, neby = i + d[0], j + d[1]
                        if 0 <= nebx < len(grid) and 0 <= neby < len(grid[0]) and grid[nebx][neby] == '1':
                            ufhelper.union((i, j), (nebx, neby))
        return ufhelper.count


    
class UnionFind:
    def __init__(self, grid):
        self.parents = {}
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.count += 1
                    self.parents[(i, j)] = (i, j)
    
    def find(self, node):
        if node == self.parents[node]:
            return node
        p = self.find(self.parents[node])
        self.parents[node] = p 
        return p 
    
    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 != p2:
            self.parents[p1] = p2
            self.count -= 1
