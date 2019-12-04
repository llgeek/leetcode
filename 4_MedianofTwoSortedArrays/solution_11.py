"""
find k-th element idea
"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      def findKthElement(nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
          return findKthElement(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
          return nums2[start2 + k - 1]
        if k == 1:
          return min(nums1[start1], nums2[start2])
        i, j = start1 + min(len1, k//2) - 1, start2 + min(len2, k//2) - 1
        if nums1[i] > nums2[j]:
          return findKthElement(nums1, start1, end1, nums2, j+1, end2, k - (j - start2 + 1))
        else:
          return findKthElement(nums1, i+1, end1, nums2, start2, end2, k - (i - start1 + 1))
      med_left = (len(nums1) + len(nums2) + 1) // 2
      med_right = (len(nums1) + len(nums2) + 2) // 2
      print(findKthElement(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, med_left))
      print(findKthElement(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, med_right))
      return (findKthElement(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, med_left) + 
              findKthElement(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, med_right)) / 2


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(sol.findMedianSortedArrays(nums1, nums2))
