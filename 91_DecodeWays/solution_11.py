"""
second trial

use DP to optimize the solution
"""


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]


if __name__ == "__main__":
    s = "1787897759966261825913315262377298132516969578441236833255596967132573482281598412163216914566534565"
    sol = Solution()
    print(sol.numDecodings(s))
