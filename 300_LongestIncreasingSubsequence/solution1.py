from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = [0] * len(nums)
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums[:idx1]):
                if dp[idx2] == 0:
                    dp[idx2] = 1
                tmp = (val1 > val2) + dp[idx2]
                if val1 > val2:
                    dp[idx1] = max(dp[idx1], dp[idx2] + 1)
            if dp[idx1] == 0:
                dp[idx1] = 1
        return max(dp)
                
if __name__ == "__main__":
    nums = [4,10,4,3,8,9]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
        