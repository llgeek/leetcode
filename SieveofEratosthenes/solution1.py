"""
Segmented Sieve

Sieve of Eratosthenes takes O(n) space, which may not fit in memory

segmented Sieve:
O(sqrt(n)) space complexity

https://www.geeksforgeeks.org/segmented-sieve/
"""

from math import sqrt, floor
class Solution():
    def __init__(self):
        self.primes = []
        
    def simpleSieve(self, seglen):
        mark = [True for _ in range(seglen+1)]
        p = 2
        while p * p < len(mark):
            if mark[p]:
                for i in range(2*p, len(mark), p):
                    mark[i] = False
            p += 1
        #self.primes = [i for i, v in enumerate(mark) if v]
        self.primes = [i for i in range(2, seglen+1) if mark[i]]

    
    def numofPrimes(self, n):
        seglen = floor(sqrt(n))
        self.simpleSieve(seglen)
        low, high = seglen, seglen*2
        while low < n:
            high = min(high, n)
            mark = [True for _ in range(seglen)]
            for p in self.primes:
                svp = floor(low / p) * p
                svp = svp if svp > low else svp + p
                for v in range(svp, high+1, p):
                    mark[v-low-1] = False
            # for i, v in enumerate(mark):
            for i in range(0, min(seglen, high - low)):
                if mark[i]: self.primes.append(i+low+1)

            low += seglen
            high += seglen
        return self.primes
    
        
if __name__ == '__main__':
    print(Solution().numofPrimes(1000))
