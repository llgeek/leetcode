class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return True
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i + 1 < m and j + 1 < n and matrix[i][j] != matrix[i+1][j+1]:
                    retrun False
        return True