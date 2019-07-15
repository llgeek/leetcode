"""
DP solution, reduce recursive time complexity
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        def dp(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            else:
                ans = False
                if j >= len(p):
                    ans = i == len(s)
                # elif i == len(s):
                #     ans = j + 1 < len(p) and p[j+1] == '*' and dp(i, j+2)
                # else:
                #     if j + 1 < len(p) and p[j+1] == '*':
                #         ans = dp(i, j+2) or (p[j] in {s[i], '.'} and dp(i+1, j))
                #     else:
                #         ans = p[j] in {s[i], '.'} and dp(i+1, j+1)
                else:
                    firstmatch = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or firstmatch and dp(i+1, j)
                    else:
                        ans = firstmatch and dp(i+1, j+1)
                self.memo[(i, j)] = ans
                return ans
        return dp(0, 0)
    
if __name__ == "__main__":
    s = "ab"
    p = ".*c"
    sol = Solution()
    print(sol.isMatch(s, p))