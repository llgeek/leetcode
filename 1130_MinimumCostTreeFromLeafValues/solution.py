"""
problem translated to:

Given an array A, choose two neighbors in the array a and b,
we can remove the smaller one min(a,b) and the cost is a * b.
What is the minimum cost to remove the whole array until only one left?

Use monotonic stack
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [(1<<31)-1]
        for val in arr:
            while stack and stack[-1] < val:
                mid = stack.pop()
                res += mid * min(stack[-1], val)
            stack.append(val)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res