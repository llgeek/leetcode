"""
another idea is to firstly find the rotation point, O(logn) time 
then either:
1. calculate the real mid point, based on the rotation index
2. use standard binary search, since we know where the target value located

"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def rotate_idx():
            start, end = 0, len(nums)-1
            while start < end:
                mid = (start + end)//2
                if nums[mid] <= nums[end]:
                    end = mid
                else:
                    start = mid+1
            return start
        def binary_search(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid+1
            return -1

        if not nums:
            return -1
        rotid = rotate_idx()
        if nums[rotid] <= target <= nums[-1]:
            return binary_search(rotid, len(nums)-1)
        else:
            return binary_search(0, rotid-1)  
        

if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [5,1,3]
    # nums = [3, 5, 1]
    target = 3
    # nums = [4,5,6,7,0,1,2]
    # target = 3
    # nums = [1]
    # target = 1
    sol = Solution()
    print(sol.search(nums, target))
