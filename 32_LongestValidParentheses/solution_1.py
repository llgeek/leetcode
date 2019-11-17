# DP

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        for i, c in enumerate(s):
          if c == ')':
            if i - 1 >= 0 and s[i-1] == '(':
              dp[i] = 2 + (dp[i-2] if i-2 >= 0 else 0)
            elif i - 1 >= 0 and s[i-1] == ')':
              if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = 2 + dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
        return max(dp)
