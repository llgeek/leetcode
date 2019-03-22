class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)


        # if not nums:
        #     return -float('inf')
        # res = nums[0]
        # start, end = 0, 1
        # tmpres = nums[0]
        # while end < len(nums):
        #     res = max(res, tmpres)
        #     if tmpres <= 0 <= nums[end]:
        #         start = end
        #         tmpres = nums[end]
        #     else:
        #         tmpres += nums[end]
        #     end += 1
        # return res
    
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(nums))

