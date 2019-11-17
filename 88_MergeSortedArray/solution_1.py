class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        curidx = m+n-1
        while i>= 0 and j >= 0:
          if nums1[i] > nums2[j]:
            nums1[curidx] = nums1[i]
            i -= 1
          else:
            nums1[curidx] = nums2[j]
            j -= 1
          curidx -= 1
        while i >= 0:
            nums1[curidx] = nums1[i]
            curidx -= 1
            i -= 1
        while j >= 0:
            nums1[curidx] = nums2[j]
            curidx -= 1
            j -= 1