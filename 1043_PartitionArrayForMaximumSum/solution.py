"""
DP
"""

from typing import List
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
      dp = [0 for _ in range(len(A))]
      for i in range(len(A)):
        curmax = 0
        for k in range(K):
          if 