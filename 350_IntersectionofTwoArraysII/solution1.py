from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        result = []
        for interval in cnt1.keys() & cnt2.keys():
            result.extend([interval] * min(cnt1[interval], cnt2[interval]))
        return result


