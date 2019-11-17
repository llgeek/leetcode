class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(i, j):
          if self.length[i][j] != 0:
            return self.length[i][j]
          tmpres = 1
          for neb in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
            ni, nj = i + neb[0], j + neb[1]
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] < matrix[i][j]:
              tmpres = max(tmpres, 1 + dfs(ni, nj))
          self.length[i][j] = tmpres
          return tmpres        
        
        self.length = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            res = max(res, dfs(i, j))
        return res
        