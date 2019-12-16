class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        curidx = m + n - 1
        while i >= 0 or j >= 0:
            val1 = nums1[i] if i >= 0 else -1<<31
            val2 = nums2[j] if j >= 0 else -1<<31
            if val1 > val2:
                i -= 1
                nums1[curidx] = val1
            else:
                j -= 1
                nums1[curidx] = val2
            curidx -= 1