from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3:
            return True
        ctype = -1
        for i in range(1, len(A)):
            if ctype == -1:
                if A[i] != A[i-1]:
                    ctype = A[i-1] > A[i]
            elif A[i] != A[i-1] and ((A[i-1] > A[i]) ^ ctype):
                    return False
        return True