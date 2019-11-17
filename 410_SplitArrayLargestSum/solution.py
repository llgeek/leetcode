from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def binaryHelper(upperbound):
          splitnum = 0
          accsum = 0
          for i in range(len(nums)):
            if accsum + nums[i] > upperbound:
              splitnum += 1
              accsum = nums[i]
            else:
              accsum += nums[i]
            if splitnum > m: return False
          splitnum += (accsum > 0)
          return splitnum <= m
        
        left, right = max(nums), sum(nums)
        while left < right:
          mid = left + (right - left) // 2
          possible = binaryHelper(mid)
          if not possible:
            left = mid + 1
          else:
            right = mid
        return left

if __name__ == "__main__":
    nums = [7,2,5,10,8]
    m = 2
    sol = Solution()
    print(sol.splitArray(nums, m))
