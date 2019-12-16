class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path, idx):
            if idx == len(nums):
                res.append(path[:])
                return
            helper(path, idx+1)
            helper(path + [nums[idx]], idx + 1)
        helper([], 0)
        return res