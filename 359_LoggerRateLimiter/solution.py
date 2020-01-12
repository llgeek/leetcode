class Solution:
    def __init__(self):
        self.window = {}
        self.limit = 10
    def rate_limiter(self, time, msg):
        if msg in self.window and time - self.window[msg] < self.limit:
            return False
        self.window[msg] = time
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.rate_limiter(1, 'foo'))
    print(sol.rate_limiter(2, 'bar'))
    print(sol.rate_limiter(3, 'foo'))
    print(sol.rate_limiter(8, 'bar'))
    print(sol.rate_limiter(10, 'foo'))
    print(sol.rate_limiter(11, 'foo'))
