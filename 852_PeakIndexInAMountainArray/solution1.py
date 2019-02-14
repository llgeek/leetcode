"""
binary search

O(log n) time complexity
"""

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A)-1
        while left <= right:
            if left == right:
                return left
            mid = (left+right) >> 1
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
