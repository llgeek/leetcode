class Solution:
    def fib(self, N: int) -> int:
        pre, cur = 0, 1
        for i in range(N):
            cur = pre + cur
            pre, cur = cur, pre
        return pre