class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        mod2idx = {0:-1}
        accsum = 0
        for i in range(len(nums)):
            accsum += nums[i]
            if k != 0:
              accsum %= k
            if accsum in mod2idx:
              if i - mod2idx[accsum] > 1:
                  return True
            else:
              mod2idx[accsum] = i
        return False


        # if k == 0: 
        #   for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] == 0:
        #       return True
        #   return False
        # k = abs(k)
        # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # for i in range(len(nums)):
        #   dp[i][i] = nums[i] % k
        # for l in range(1, len(nums)):
        #   for i in range(len(nums)):
        #     j = i + l
        #     if j >= len(nums) - 1:
        #       break
        #     dp[i][j] = (dp[i][j-1] + nums[j]) % k
        #     if dp[i][j] == 0:
        #       return True
        # return False
