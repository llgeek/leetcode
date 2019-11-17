class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, j = 0, len(nums)-1
        while i < j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else: i += 1
        return i if nums[i] == val else i + 1