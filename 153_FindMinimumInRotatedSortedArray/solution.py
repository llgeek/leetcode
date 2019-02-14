class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            # if nums[left] > nums[right]:
            #     if nums[mid] > nums[left]:
            #         left = mid + 1
            #     else:
            #         right = mid
            # else:
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            