from typing import List
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
      dp = {}
      for i in range(1, len(A)):
        for j in range(i):
          diff = A[i] - A[j]
          dp[diff, i] = max(dp.get((diff, i), 1), dp.get((diff, j),  1) + 1)
      return max(dp.values())

if __name__ == "__main__":
    sol = Solution()
    A = [3,6,9,12]
    print(sol.longestArithSeqLength(A))