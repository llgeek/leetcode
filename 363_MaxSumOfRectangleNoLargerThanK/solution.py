from typing import List
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not any(matrix):
            return 0
        INT_MIN = - 1 << 31
        res = INT_MIN
        for i in range(len(matrix[0])):
            curtmp = [0 for _ in range(len(matrix))]
            for j in range(i, len(matrix[0])):
                for r in range(len(matrix)):
                    curtmp[r] += matrix[r][j]

                cum_sum = [0]
                max_sum, sum_so_far = INT_MIN, 0
                for x in curtmp:
                    sum_so_far += x
                    left = bisect.bisect_left(cum_sum, sum_so_far - k)
                    if left < len(cum_sum):
                        max_sum = max(max_sum, sum_so_far - cum_sum[left])
                    bisect.insort(cum_sum, sum_so_far)
                res = max(res, max_sum)
        return res


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    print(sol.maxSumSubmatrix(matrix, k))