"""
second trial
"""
import math
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        def chooseTwo(one, two):
            return math.factorial(one+two) // (math.factorial(two)*math.factorial(one))

        one = n
        two = 0
        res = 0
        while one >= 0:
            res += chooseTwo(one, two)
            one -= 2
            two += 1
        return res

if __name__ == "__main__":
    n = 2
    sol = Solution()
    print(sol.climbStairs(n))