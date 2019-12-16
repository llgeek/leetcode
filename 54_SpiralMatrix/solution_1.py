from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def yield_idx(r1, r2, c1, c2):
            for j in range(c1, c2+1):
                yield r1, j
            for i in range(r1+1, r2+1):
                yield i, c2
            if r1 < r2 and c1 < c2:
                for j in range(c2-1, c1-1, -1):
                    yield r2, j
                for i in range(r2-1, r1, -1):
                    yield i, c1
        
        res = []
        if not any(matrix): return res
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for i, j in yield_idx(r1, r2, c1, c2):
                res.append(matrix[i][j])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
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