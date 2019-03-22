class Solution:
    def isValid(self, s: 'str') -> 'bool':
        parenthesis = {']': '[', ')':'(', '}': '{'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack[-1] != parenthesis[c]:
                    return False
                else:
                    stack.pop()
        return not stack