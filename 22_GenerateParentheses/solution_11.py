class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      self.res = []
      def backtracker(n, par, left, right):
        if left == right == n:
          self.res.append(par)
          return
        if left <= right:
          backtracker(n, par+'(', left+1, right)
        else:
          backtracker(n, par+')', left, right+1)
          if left < n:
            backtracker(n, par+'(', left+1, right)
      backtracker(n, '', 0, 0)
      return self.res