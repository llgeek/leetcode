class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []
        for _ in range(m * n):
          if (i + j) % 2 == 0: #move up
            if i == 0:
              j += 1
            elif j == len(matrix)-1:
              i -= 1
            else:
              i -= 1
              j += 1
          else:
            if i == len(matrix)-1:
              j -= 1
            elif j == 0:
              i += 1
            else:
              i += 1
              j -= 1
        return res