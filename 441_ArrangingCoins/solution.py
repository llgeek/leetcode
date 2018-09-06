from math import sqrt, floor
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(floor(sqrt(2*n)), -1, -1):
            if i*(i+1) <= 2*n and (i+1)*(i+2) > 2*n:
                return i 
        return 0

