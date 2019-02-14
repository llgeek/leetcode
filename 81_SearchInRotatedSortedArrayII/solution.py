
"""

The only difference is the duplicate, where 
nums[left] == nums[right] == nums[mid]

in this case, we have to linearly decrease right or increase left by one

The average time complexity is O(logn)
but for worst case, it could be O(n)

"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 2
    sol = Solution()
    print(sol.search(nums, target))
