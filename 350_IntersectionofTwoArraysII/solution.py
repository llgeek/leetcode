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
        for c in set(cnt1.keys()) & set(cnt2.keys()):
            times = min(cnt1[c], cnt2[c])
            result.extend([c] * times)
        return result


if __name__ == '__main__':
    nums1 = [3,1,2]
    nums2 = [1,1]
    print(Solution().intersect(nums1, nums2))
