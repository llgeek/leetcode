from typing import List
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def helper(A, B):
            a, b = 0, 0
            for i in range(len(A)):
                if A[i] != A[0] and B[i] != A[0]:
                    break
                if A[i] != A[0]:
                    a += 1
                if B[i] != A[0]:
                    b += 1
                if i == len(A) - 1:
                    return min(a, b)
            return -1

        res1, res2 = helper(A, B), helper(B, A)
        return -1 if res1 == res2 == -1 else min(res for res in (res1, res2) if res != -1)
