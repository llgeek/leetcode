"""
dynamic programming (closure number)
"""



class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        memo = {}
        memo[0] = {''}
        memo[1] = {'()'}
        for i in range(2, n+1):
            memo[i] = set()
            for k in range(i):
                if k == 0:
                    for par in memo[i-1]:
                        memo[i].add('('+par+')')
                else:
                    for par1 in memo[k]:
                        for par2 in memo[i-k]:
                            memo[i].add(par1 + par2)
        return list(memo[n])

if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))

