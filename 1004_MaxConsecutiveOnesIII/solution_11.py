from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
      res = 0
      pre, cur = 0, 0
      while cur < len(A):
        if A[cur] == 0:
          K -= 1
        while K < 0:
          if A[pre] == 0:
            K += 1
          pre += 1
        res = max(res, cur - pre + 1)
        cur += 1
      return res