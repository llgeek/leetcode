#Union and find idea
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        distance = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        ufhelper = UnionFind(grid)
        m, n = m, n = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    for dx, dy in distance:
                        newi, newj = i + dx, j + dy
                        if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == '1':
                            ufhelper.union(i * n + j, newi * n + newj)
        return ufhelper.count
                    
                    

class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.parents = [0] * (m * n)
        self.count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    idx = i * n + j
                    self.parents[idx] = idx
                    self.count += 1
    
    def find(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        node1p = self.find(node1)
        node2p = self.find(node2)
        if node1p != node2p:
            self.parents[node2p] = node1p
            self.count -= 1


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
        
print(Solution().numIslands(grid))
