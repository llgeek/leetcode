class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        cur = 0
        stack = []
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0
            elif c == ')':
                cur = stack.pop() + max(2 * cur, 1)
        return cur
