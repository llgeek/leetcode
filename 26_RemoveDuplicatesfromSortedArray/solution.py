class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1
        # if not nums:
        #     return 0
        # curnum = nums[0]
        # curidx = 0
        # for ptr in range(1, len(nums)):
        #     num = nums[ptr]
        #     if num == curnum:
        #         continue
        #     else:
        #         curidx += 1
        #         nums[curidx], nums[ptr] = nums[ptr], nums[curidx]
        #         curnum = nums[curidx]
                
        # print(nums)
        # return curidx + 1

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
