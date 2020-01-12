from typing import List
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        s1, n1 = 1, 0
        for i in range(1, N):
            s2 = n2 = N
            if A[i-1] < A[i] and B[i-1] < B[i]:
                s2 = min(s1 + 1, s2)
                n2 = min(n2, n1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                s2 = min(n1 + 1, s2)
                n2 = min(s1, n2)
            s1, n1 = s2, n2
        return min(s1, n1)