class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        while cur < len(nums):
            if cur - 1 >= 0 and nums[cur-1] == nums[cur]:
              cur += 1
            else:
              firstval = nums[cur]
              nums[prev], nums[cur] = nums[cur], nums[prev]
              cur += 1
              prev += 1
              if cur < len(nums) and nums[cur] == firstval:
                nums[prev], nums[cur] = nums[cur], nums[prev]
                cur += 1
                prev += 1
              while cur < len(nums) and nums[cur] == firstval:
                cur += 1
        return prev
