
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not any(matrix):
            return False
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n-1
        while 0 <= x < m and 0 <= y < n:
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                y -= 1
            elif target > matrix[x][y]:
                x += 1
        return False
