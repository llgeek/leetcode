"""
recursive:
time complexity: O((T+P)2^(T+P/2))
space complexity: O((T+P)2^(T+P/2))

DP:
time complexity: O(TP)
space complexity: O(TP)

"""



class Solution:
    def isMatch_recursive(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        This is the recursive version, while it will TLE in leetcode
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch_recursive(s, p[2:])) or (first_match and self.isMatch_recursive(s[1:], p))
        else:
            return first_match and self.isMatch_recursive(s[1:], p[1:])


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        revise the recursive version into DP
        top-down variation
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = (i < len(s)) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i,j] = ans
            return memo[i,j]
        return dp(0,0)

    def isMatch_bottomup(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        revise the recursive version into DP
        bottom up variation
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]



    
if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    sol = Solution()
    print(sol.isMatch_recursive(s, p))
    print(sol.isMatch(s, p))
    print(sol.isMatch_bottomup(s, p))
        
