class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtracker(nums, begin):
            if begin >= len(nums):
                self.res.append(nums[:])
                return
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                backtracker(nums, begin+1)
                nums[i], nums[begin] = nums[begin], nums[i]
        backtracker(nums, 0)
        return self.res