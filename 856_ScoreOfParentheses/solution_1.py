class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        cur = 0
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + max(2 * cur, 1)
        return cur