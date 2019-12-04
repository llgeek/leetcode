import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        if not n:
            return (nums1[(m+n)//2] + nums1[(m+n+1)//2]) / 2
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            # need to increase i
            if j != 0 and i != imax and nums1[i] < nums1[j-1]:
                imin = i + 1
            # need to decrease i
            elif i != 0 and j != n and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m+n) & 1:
                    return max_of_left
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                return (min_of_right + max_of_left) / 2.