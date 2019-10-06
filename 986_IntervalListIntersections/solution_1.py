from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        # left, right = (1<<31)-1, -1<<31
        res = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]:
                j += 1
            else:
                res.append((max(A[i][0], B[j][0]), min(A[i][1], B[j][1])))
                if A[i][1] < B[j][1]: i += 1
                else: j += 1
        return res