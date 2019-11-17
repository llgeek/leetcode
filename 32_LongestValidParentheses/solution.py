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
                if stack:
                    stack.pop()
                if not stack: 
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
        return maxlen

if __name__ == "__main__":
    # s = ")()())"
    s = "())((()))"
    sol = Solution()
    print(sol.longestValidParentheses(s))
                    


