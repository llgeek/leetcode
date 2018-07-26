class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        presum = dict()
        presum[0] = 1
        accsum = 0
        for num in nums:
            accsum += num
            count += presum.get(accsum-k, 0)
            presum[accsum] = presum.get(accsum, 0) + 1
        return count


if __name__ == "__main__":
    nums = [-1, 0,0,0,1]
    k = 0
    print(Solution().subarraySum(nums, k))
                
                
        