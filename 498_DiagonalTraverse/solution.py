class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        direct = 'up'
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []
        while i < len(matrix) or j < len(matrix[0]):
          res.append(matrix[i][j])
          if direct == 'up':
            if j == len(matrix[0])-1:
              i += 1
              direct = 'down'
            elif i == 0:
              j += 1
              direct = 'down'
            
            else:
              i -= 1
              j += 1
          else:
            if i == len(matrix)-1:
              j += 1
              direct = 'up'
            elif j == 0:
              i += 1
              direct = 'up'
            else:
              i += 1
              j -= 1
        return res