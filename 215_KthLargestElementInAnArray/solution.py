class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, start, end):
            if start > end:
                return 0
            i= start - 1
            for j in range(start, end):
                if nums[j] > nums[end]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[end] = nums[end], nums[i]
            return i - start + 1

        def helper(nums, start, end, k):
            q = partition(nums, start, end)
            if q < k:
                return helper(nums, start+q, end, k-q)
            elif q > k:
                return helper(nums, start, start+q-2, k)
            else:
                return nums[start+q-1]

        return helper(nums, 0, len(nums)-1, k)

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    print(sol.findKthLargest(nums, k))
