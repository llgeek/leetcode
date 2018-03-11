class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        minnum = min(nums)
        maxnum = max(nums)
        bucketsize = max(1, (maxnum - minnum) // (len(nums)-1))
        bucketnum = (maxnum - minnum) //bucketsize + 1

        buckets = [Bucket() for _ in range(bucketnum)]
        for num in nums:
            idx = (num-minnum) // bucketsize
            buckets[idx].used = True
            buckets[idx].minval = min(num, buckets[idx].minval)
            buckets[idx].maxval = max(num, buckets[idx].maxval)
        prebucketmax, maxgap = minnum, 0

        for bucket in buckets:
            if bucket.used:
                maxgap = max(maxgap, bucket.minval - prebucketmax)
                prebucketmax = bucket.maxval
        return maxgap


class Bucket:
    def __init__(self):
        self.used = False
        self.minval = 0xFFFFFFFF
        self.maxval = -0xFFFFFFFF


s = Solution()
nums = [1, 9, 13, 2]
print(s.maximumGap(nums))