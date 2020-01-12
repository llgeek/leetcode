from typing import List
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        cntA = {i: 0 for i in range(1, 7)}
        cntB = {i: 0 for i in range(1, 7)}
        same = {i: 0 for i in range(1, 7)}
        for i in range(len(A)):
            cntA[A[i]] += 1
            cntB[B[i]] += 1
            if A[i] == B[i]:
                same[A[i]] += 1
        for i in cntA.keys():
            if cntA[i] + cntB[i] - same[i] == len(A):
                return len(A) - max(cntA[i], cntB[i])
        return -1

    # much shorter version
    def minDominoRotations2(self, A: List[int], B: List[int]) -> int:
        for x in ([A[0], B[0]]):
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1