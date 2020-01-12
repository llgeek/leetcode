"""
Prev/Next array

given index j,
in prev array, find index i (i <= j) that A[i] < A[j]
in next array, find index k (k > j) that A[k] >= A[j]
"""
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        prev = [None] * len(A)
        for i in range(len(A)):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        nex = [None] * len(A)
        for k in range(len(A)-1, -1, -1):
            while stack and A[stack[-1]] > A[k]:
                stack.pop()
            nex[k] = stack[-1] if stack else len(A)
            stack.append(k)
        MOD = 10 ** 9 + 7
        return sum((i - prev[i]) * (nex[i] - i) * A[i] for i in range(len(A))) % MOD

            
            
        