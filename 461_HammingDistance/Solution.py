class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        k = 1
        count = 0
        for i in range (31):
            if ((x & k) != (y & k)):
                count = count + 1
            k = k << 1
        return count
            