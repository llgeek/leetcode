class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return -1
        nums.sort()
        n = len(nums)
        pre = 0, nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] != pre[1]:
                if i - pre[0] > n // 3:
                    res.append(pre[1])
                pre = i, nums[i]
        if len(nums) - pre[0] > n // 3:
            res.append(nums[-1])
        return res
