import random
class Solution:

    def __init__(self, nums: List[int]):
      self.nums = nums
        

    def pick(self, target: int) -> int:
        cnt = 0
        res = 0
        for i, num in enumerate(self.nums):
          if num == target:
            prob = random.randint(0, cnt)
            res = i if prob == 0 else res
            cnt += 1
        return res





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)