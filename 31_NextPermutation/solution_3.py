class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_increase = len(nums)-1
        while first_increase:
          if nums[first_increase] > nums[first_increase - 1]:
            break
          first_increase -= 1
        if not first_increase:
          nums.reverse()
          return 
        diff = nums[first_increase] - nums[first_increase-1]
        swapidx = first_increase
        for j in range(len(nums)-1, first_increase-1, -1):
          if nums[j] > nums[first_increase-1] and (nums[j] - nums[first_increase]) < diff:
            diff = nums[j] - nums[first_increase]
            swapidx = j
        
        nums[first_increase-1], nums[swapidx] = nums[swapidx], nums[first_increase-1]
        nums[first_increase:] = nums[first_increase:][::-1]
