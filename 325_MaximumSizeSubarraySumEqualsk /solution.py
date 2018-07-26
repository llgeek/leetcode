class Solution:
    def maxSubArrayLen(self, nums, k):
        maxlen = 0
        presum = dict()
        accsum = 0
        for idx, num in enumerate(nums):
            accsum += num
            # if num == k:
            #     maxlen = max(maxlen, 1)
            if accsum == k:
                maxlen = idx+1
            if accsum - k in presum:
                maxlen = max(maxlen, idx-presum[accsum-k])
            if accsum not in presum:
                presum[accsum] = idx
        return maxlen


if __name__ == '__main__':
    # nums = [1, -1, 66, -2, 3]
    nums = [-1, 0,0,0,2]
    k = 0
    print(Solution().maxSubArrayLen(nums, k))