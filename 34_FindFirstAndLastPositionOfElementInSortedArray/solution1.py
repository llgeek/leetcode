from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res

        # find left idx
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i += 1
            else:
                j = mid
        if nums[i] == target:
            res[0] = i
        # i, j = 0, len(nums)
        # while i < j:
        #     mid = (i + j) // 2
        #     if nums[mid] > target:
        #         j = mid
        #     else:
        #         i = mid + 1
        # if nums[j-1] == target:
        #     res[1] = j-1
        j = len(nums)-1
        while i < j:
            mid = (i + j) // 2 + 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        if nums[j] == target:
            res[1] = j
        return res