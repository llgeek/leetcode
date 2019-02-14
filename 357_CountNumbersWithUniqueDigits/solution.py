class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial
        def nAr(n, r):
            ret = 1
            for i in range(n, n-r, -1):
                ret *= i
            return ret
            
        if n == 0:
            return 1
        num = [0] * (n+1)
        num[0] = 1
        for i in range(1,n+1):
            num[i] = nAr(10, i) - nAr(9, i-1)
        return sum(num)

if __name__ == "__main__":
    n = 1
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(n))