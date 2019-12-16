class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0.:
            return 0.
        if x == 1.0:
            return 1.0
        if x == -1.0:
            return -1.0 if n & 1 else 1.0
        if n == -1<<31:
            return 0
        if n < 0:
            x = 1/x
            n = -n
        return x * self.myPow(x**2, n//2) if n & 1 else self.myPow(x**2, n//2)