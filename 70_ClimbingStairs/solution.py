class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(m):
            ret = 0
            for i in range(m):
                ret += (numways[i] * numways[m-i])
            return ret
        if n <= 2:
            return max(0, n)
        numways = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            numways[i] = helper(i) - (i - 2)
        return numways[n]

if __name__ == '__main__':
    n =  3
    print(Solution().climbStairs(n))

