


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        inchr = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in inchr:
                stack.append(c)
            else:
                if stack and stack[-1] in inchr and inchr[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    # s = "([)]"
    s= ']'
    sol = Solution()
    print(sol.isValid(s))
