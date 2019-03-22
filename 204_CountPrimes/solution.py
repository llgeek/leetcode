class Solution:
    def countPrimes(self, n: int) -> int:
        notPrime = [False] * n
        res = 0
        for i in range(2, n):
            if not notPrime[i]:
                res += 1
                for j in range(2, n):
                    if i * j >= n: break
                    notPrime[i*j] = True
        return res

if __name__ == "__main__":
    n = 10
    sol = Solution()
    print(sol.countPrimes(n))

