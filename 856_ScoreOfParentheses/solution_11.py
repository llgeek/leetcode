class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        bal = 0
        for i in range(len(S)):
            if S[i] == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans