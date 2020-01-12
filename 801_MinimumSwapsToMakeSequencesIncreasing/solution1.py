from typing import List
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        swapped = [N] * N
        not_swapped = [N] * N
        res = N
        swapped[0], not_swapped[0] = 1, 0
        for i in range(1, len(A)):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                not_swapped[i] = not_swapped[i-1]
                swapped[i] = swapped[i-1] + 1
            if A[i-1] < B[i] and B[i-1] < A[i]:
                swapped[i] = min(not_swapped[i-1] + 1, swapped[i])
                not_swapped[i] = min(swapped[i-1], not_swapped[i])
        return min(not_swapped[-1], swapped[-1])