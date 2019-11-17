from typing import List
import math
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        nums = [0] * 121
        for age in ages:
            nums[age] += 1
        res = 0
        for A in range(1, 121):
            lowerB = math.floor(0.5*A+7) + 1
            res += nums[A] * max(sum(nums[lowerB:A+1]) - 1, 0)
        # for A in range(1, 100):
        return res

if __name__ == "__main__":
    ages = [16,17,18]
    sol = Solution()
    print(sol.numFriendRequests(ages))
        