from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A
        MAXNUM, MINNUM = (1 << 31) - 1, - 1 << 31
        res = []
        idx = 0
        while idx < len(A) and A[idx] < 0:
            idx += 1
        left, right = idx-1, idx
        while left >= 0 or right < len(A):
            leftsqr = A[left] ** 2 if left >= 0 else MAXNUM
            rightsqr = A[right] ** 2 if right < len(A) else MAXNUM
            if leftsqr > rightsqr:
                res.append(rightsqr)
                right += 1
            else:
                res.append(leftsqr)
                left -= 1
        return res

if __name__ == "__main__":
    sol = Solution()
    A = [-1]
    print(sol.sortedSquares(A))