class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        maxlen = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if not stack:
                    stack.append(i)
                    continue
                if 0 <= stack[-1] < len(s) and s[stack[-1]] == '(':
                    stack.pop()
                    maxlen = max(maxlen, (i-stack[-1]))
                    


