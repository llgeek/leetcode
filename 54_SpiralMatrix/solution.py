import math
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []
        m, n = len(matrix), len(matrix[0])
        res = [0] * (len(matrix)*len(matrix[0]))
        i, j = 0, 0
        dirt = (0, 1)
        direc = 'left'
        rnd = 0
        for idx in range(m*n):
            res[idx] = matrix[i][j]
            if direc == 'left' and j == n-rnd-1:
                direc = 'down'
                dirt = (1, 0)
            elif direc == 'down' and i == m-rnd-1:
                direc = 'right'
                dirt = (0,-1)
            elif direc == 'right' and j == rnd:
                direc = 'up'
                dirt = (-1, 0)
            elif direc == 'up' and i == rnd+1:
                rnd += 1
                direc = 'left'
                dirt = (0, 1)
            i += dirt[0]
            j += dirt[1]
        return res

if __name__ == "__main__":
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    sol = Solution()
    print(sol.spiralOrder(matrix))


