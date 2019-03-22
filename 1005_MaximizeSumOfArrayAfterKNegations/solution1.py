class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(len(A)):
            if K == 0 or A[i] >= 0:
                break
            A[i] = -A[i]
            K -= 1
        res, minval = 0, float('inf')
        for val in A:
            res += val
            minval = min(minval, val)
        return res - (K % 2) * 2 * minval