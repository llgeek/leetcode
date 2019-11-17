class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        idxs = []
        stack = []
        for idx, c in enumerate(S):
          if c == '(':
            if not stack:
              idxs.append(idx)
            stack.append(c)
          elif c == ')':
            assert not stack
            stack.pop()
            if not stack:
              idxs.append(idx)
        i, j = 0, 0
        res = []
        while j < len(S) and i < len(idxs):
          if j == idxs[i]:
            i += 1
          else:
            res.append(S[j])
          j += 1
        while j < len(S):
          res.append(S[j])
          j += 1
        return "".join(res)
