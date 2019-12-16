class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        mapping = dict(zip(map(str, range(1, 27)), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if s[0] not in mapping: return 0
        
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if s[i-1:i+1] in mapping:
                dp[i] += dp[i-2] if i-2 >= 0 else 1
        return dp[len(s)-1]