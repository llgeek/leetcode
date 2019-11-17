class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, last = 0, len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return i