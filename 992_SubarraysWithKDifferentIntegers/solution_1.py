from typing import List
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostKDistinct(A, K) - self.atMostKDistinct(A, K-1)
    
    def atMostKDistinct(self, A, K):
      left, right = 0, 0
      res = 0
      chr2freq = {}
      distinctnum = 0
      while right < len(A):
        if chr2freq.get(A[right], 0) == 0:
          distinctnum += 1
        chr2freq[A[right]] = chr2freq.get(A[right], 0) + 1
        while distinctnum > K and left <= right:
          chr2freq[A[left]] -= 1
          if chr2freq[A[left]] == 0:
            distinctnum -= 1
          left += 1
        res += (right - left + 1)
        right += 1
      return res
