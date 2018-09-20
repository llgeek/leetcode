"""https://www.geeksforgeeks.org/sieve-of-eratosthenes/

Sieve of Eratosthenes

time complexity: O(n loglog n)
"""



class Solution():
    def numofPrimes(self, n):
        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(2*p, n+1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(2, n+1) if primes[i]]
        
        


if __name__ == '__main__':
    print(Solution().numofPrimes(1000))
