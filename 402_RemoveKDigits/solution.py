"""
DP
dp[i][k] represents num[0...i] removing k digits, minimum value
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
      if not num or len(num) <= k:
        return 0
      dp = [[0 for i in range(k+1)] for _ in range(len(num))]
      dp[0][0] = int(num[0])
      for i in range(1, len(num)):
        dp[i][0] = dp[i-1][0] * 10 + int(num[i])
      for j in range(1, k+1):
        for i in range(j, len(num)):
          dp[i][j] = min(dp[i][j-1], dp[i-1][j] * 10 + int(num[i]))
      return dp[len(num)-1][k]


      def removeKdigits(self, num: str, k: int) -> str:
        self.memo = {}
        def helper(idx, k):
          if k >= idx + 1:
            self.memo[(idx, k)] = 0
            return 0
          if idx -1 >= 0 and (idx-1, k) in self.memo:
            

        