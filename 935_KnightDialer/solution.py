"""

wrong answer, didn't understand the meaning of the problem!
"""

class Solution:
    def knightDialer(self, N: int) -> int:
      if N == 0: return 0
      # self.memo = {0: dict(zip(range(10), range(10)))}
      # self.memo = {(N-1, i): [i] for i in range(10)}
      self.memo = {}
      self.move = {0: (4,6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9), 5: (), 6: (1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
      MOD = 10**9+7

      def move_next(reststep, start):
        if reststep == 1:
          self.memo[1, start] = [start]
          return [start]
        if (reststep, start) in self.memo:
          return self.memo[reststep, start]
        else:
          reachable = []
          for nextstart in self.move[start]:
            nextvals = move_next(reststep-1, nextstart)
            if nextvals:
              reachable.extend(nextvals)
          self.memo[reststep, start] = list(set([(start * 10 + val) % MOD for val in reachable]))

      if N == 0: return 0
      for start in range(10):
        move_next(N, start)
      print(self.memo)
      return sum(len(self.memo[N, start]) for start in range(10)  if (N, start) in self.memo)
      
if __name__ == "__main__":
    N = 2
    print(Solution().knightDialer(N))


          