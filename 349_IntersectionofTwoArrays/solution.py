class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        # from collections import Counter # is also okay, but slower
        if not nums1 or not nums2:
            return []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        cnt1 = defaultdict(lambda: 0)
        for val in nums1:
            cnt1[val] += 1
        result = []
        for val in nums2:
            if val in cnt1:
                result.append(val)
                cnt1.pop(val)
        return result
                
            
            
