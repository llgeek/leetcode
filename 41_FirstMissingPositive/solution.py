from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                expectidx = nums[i] - 1
                nums[i], nums[expectidx] = nums[expectidx], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return n + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,-1,1]
    print(sol.firstMissingPositive(nums))