# using Counter, only counter for once

from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        cnt1 = Counter(nums1)
        result = []
        for val in nums2:
            if val in cnt1 and cnt1[val] > 0:
                result.append(val)
                cnt1[val] -= 1
        return result
            
