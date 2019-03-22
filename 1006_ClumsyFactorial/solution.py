class Solution:
    def clumsy(self, N: int) -> int:
        def helper(n, first = True):
            if n == 0:
                return 0
            elif n == 1:
                return n
            elif n == 2:
                return n*(n-1)
            elif n == 3:
                return n*(n-1)//(n-2)
            else:
                tmp = n*(n-1)//(n-2)+(n-3) * (1 if first else -1)
                return tmp - helper(n-4, False)
            # elif n == 4:
            #     return n*(n-1)//(n-2)+n-3
            # else:
            #     return n*(n-1)//(n-2)+(n-3) - helper(n-4)
        
        return helper(N, True)

if __name__ == "__main__":
    N = 10
    sol = Solution()
    print(sol.clumsy(N))
