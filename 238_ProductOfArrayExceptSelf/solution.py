class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
        return res

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))
