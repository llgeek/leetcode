class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        for c in s:
          if c in pair:
            if not stack or stack[-1] != pair[c]:
              return False
            else:
              stack.pop()
          elif c in "([{":
            stack.append(c)
        return not stack
