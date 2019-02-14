class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        first, last = 0, len(nums)-1
        while first <= last:
            if nums[first] == val:
                while first < last and nums[last] == val:
                    last -= 1
                if nums[last] != val:
                    nums[first], nums[last] = nums[last], nums[first]
                    last -= 1
                else:
                    break
            first += 1
        return first

if __name__ == "__main__":
    # nums = [3,2,2,3]
    # val = 3
    nums = [1]
    val = 1
    sol = Solution()
    print(sol.removeElement(nums, val))
    print(nums)
