class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        increase = True
        curidx = 0
        maxlen = 0
        while curidx < len(A):
            