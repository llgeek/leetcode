"""
typical binary search, have to consider a lots of corner cases

1. nums[start] < nums[end]
2. nums[start] > nums[end]
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[end]:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < nums[end]:
                    if nums[start] > target > nums[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if nums[start] <= target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                
        return -1

if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [5,1,3]
    nums = [3,5,1]
    target = 3
    sol = Solution()
    print(sol.search(nums, target))
