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
        for i in range(len(A)-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            nex[i] = stack[-1] if stack else len(A)
            stack.append(i)
        return sum((i - prev[i]) * (nex[i] - i) * A[i] for i in range(len(A))) % (10 ** 9 + 7)