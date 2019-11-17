class Solution:
    def removeOuterParentheses(self, S: str) -> str:
      res = []
      left = 0
      for c in S:
        if c == '(':
          if left != 0:
            res.append(c)
          left += 1
        elif c == ')':
          if left != 1:
            res.append(c)
          left -= 1
        else:
          res.append(c)
      return "".join(res)