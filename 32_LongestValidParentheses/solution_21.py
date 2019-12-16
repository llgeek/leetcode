"""
use stack
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            elif c == ')':
                stack.pop()
                if stack:
                    res = max(res, idx - stack[-1])
                else:
                    stack.append(idx)
        return res
                
        