class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        isPalindrom = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            isPalindrom[i][i] = True
            if i < len(s)-1 and s[i] == s[i+1]:
                isPalindrom[i][i+1] = True
        for l in range(len(s)):
            for i in range(1, len(s)-l-1):
                if isPalindrom[i][i+l] and s[i-1] == s[i+l+1]:
                    isPalindrom[i-1][i+l+1] = True
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrom[i][j]:
                    res += 1
        return res

if __name__ == "__main__":
    s = 'aaa'
    sol = Solution()
    print(sol.countSubstrings(s))
        