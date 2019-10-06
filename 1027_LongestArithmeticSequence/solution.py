from typing import List
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 2
        dp = dict()
        for idx1, val1 in enumerate(A):
            for idx2, val2 in enumerate(A[:idx1]):
                dp[idx1, val1-val2] = dp.get((idx2, val1-val2), 1) + 1
                res = max(res, dp[idx1, val1-val2])
        return res