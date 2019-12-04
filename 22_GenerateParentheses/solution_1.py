class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {}
        memo[0] = {''}
        memo[1] = {'()'}
        for i in range(2, n+1):
          res = set()
          for j in range(i):
            if j == 0:
              for p in memo[i-1]:
                res.add('(' + p + ')')
            else:
              for p1 in memo[j]:
                for p2 in memo[i-j]:
                  res.add(p1 + p2)
          memo[i] = res
        return list(memo[n])
