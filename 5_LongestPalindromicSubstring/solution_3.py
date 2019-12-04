class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = 0, 0
        for i in range(len(s)):
          memo[i][i] = True
        for length in range(1, len(s)):
          for i in range(len(s)):
            j = i + length
            if j >= len(s): continue
            memo[i][j] = s[i] == s[j] and (memo[i+1][j-1] if i+1 <= j-1 else True)
            if memo[i][j] and j-i > ans[1] - ans[0]:
              ans = i, j
        return s[ans[0]:ans[1]+1]

if __name__ == "__main__":
    sol = Solution()
    # s = "babad"
    s = "cbbd"
    print(sol.longestPalindrome(s))
            
