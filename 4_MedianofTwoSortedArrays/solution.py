"""
O(log(min(m,n))) time complexity
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n = n, m 
            nums1, nums2 = nums2, nums1
        if n == 0:
            raise ValueError

        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m+n+1) // 2 - i 
            if i > 0  and nums1[i-1] > nums2[j]:
                imax = i-1
            elif i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            # if (i == 0 or j == n or nums1[i-1] <= nums2[j]) and (j == 0 or i == m or nums2[j-1] <= nums1[i]):
            #     return max(nums1[i-1], nums2[j-1]) if (m+n) % 2 else (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m+n) % 2:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
