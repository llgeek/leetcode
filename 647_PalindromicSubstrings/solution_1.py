class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
          dp[i][i] = True
          res += 1
        for l in range(1, len(s)):
          for i in range(0, len(s)):
            j = i + l
            if j >= len(s): continue
            mid = (i+1 >= j-1) or dp[i+1][j-1]
            dp[i][j] = mid and (s[i] == s[j])
            res += dp[i][j] == True
        return res