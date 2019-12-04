"""
still use DP
simply the logic of solution_4.py version
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      self.memo = {}
      def dp(i, j):
        if (i, j) in self.memo:
          return self.memo[i, j]
        if j >= len(p):
          ans = i == len(s)
        else:
          firstmatch = i < len(s) and p[j] in {s[i], '.'}
          if j + 1 < len(p) and p[j+1] == '*':
            ans = dp(i, j+2) or firstmatch and dp(i+1, j)
          else:
            ans = firstmatch and dp(i+1, j+1)
        self.memo[i, j] = ans
        return ans
      return dp(0, 0)