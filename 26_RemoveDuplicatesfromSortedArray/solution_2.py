class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        pre = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pre]:
                pre += 1
                nums[i], nums[pre] = nums[pre], nums[i]
        return pre + 1
