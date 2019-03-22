class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        while j >= 0:
            if i < 0:
                nums1[i+j+1] = nums2[j]
                j -= 1
                continue
            if nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        
if __name__ == "__main__":
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
