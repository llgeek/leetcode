# class Solution:
#     def knightDialer(self, N: int) -> int:
#       self.memo = {}
#       self.move = {0: (4,6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
#       MOD = 10**9+7
      
#       def dp(step, start):
#         if step == 0: 
#           # self.memo[0, start] = 1
#           return 0
#         if (step, start) not in self.memo: 
#           cnt = 1
#           for nextstart in self.move[start]:
#             cnt += dp(step-1, nextstart)
#           self.memo[step, start] = cnt % MOD
#         return self.memo[step, start]
      
#       if N <= 0: return 0
#       for start in range(10):
#         dp(N, start)
#       return sum(self.memo[N, start] for start in range(10) if (N, start) in self.memo)

class Solution:
    def knightDialer(self, N: int) -> int:
      move = {0: (4,6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
      dp = [1] * 10
      MOD = 10**9+7
      for reststep in range(N-1):
        dp2 = [0] * 10
        for i in range(10):
          for nextstep in move[i]:
            dp2[nextstep] += dp[i]
            dp2[nextstep] %= MOD
        dp = dp2[:]
      return sum(dp) % MOD

