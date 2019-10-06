from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A: return []
        if A[0] >= 0: return [val ** 2 for val in A]
        if A[-1] <= 0: return [val ** 2 for val in A[::-1]]
        i = 0
        while i < len(A):
            if A[i] <= 0 and A[i+1] > 0: break
            i += 1
        left, right = i, i+1
        res = []
        while left >= 0 and right < len(A):
            if -A[left] <= A[right]:
                res.append(A[left]**2)
                left -= 1
            else:
                res.append(A[right]**2)
                right += 1
        while left >= 0:
            res.append(A[left]**2)
            left -= 1
        while right < len(A):
            res.append(A[right]**2)
            right += 1
        return res

print(Solution().sortedSquares([-4,-1,0,3,10]))