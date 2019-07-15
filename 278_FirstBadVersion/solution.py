# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            sstatus = isBadVersion(start)
            if sstatus:
                return start
            # estatus = isBadVersion(end)
            mid = (start + end) // 2
            mstatus = isBadVersion(mid)
            if mstatus == True:
                end = mid
            else:
                start = mid+1
        return start
            