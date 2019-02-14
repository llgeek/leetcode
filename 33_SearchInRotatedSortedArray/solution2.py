"""
similar idea with solution1.py

still find the real rotate index, then calculate the real middle each time
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
        
        if not nums:
            return -1
        rotid = rotate_idx()
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            realmid = (mid + rotid) % len(nums)
            if target == nums[realmid]:
                return realmid
            elif target < nums[realmid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1


if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [5, 1, 3]
    # nums = [3, 5, 1]
    target = 3
    # nums = [4,5,6,7,0,1,2]
    # target = 3
    # nums = [1]
    # target = 1
    sol = Solution()
    print(sol.search(nums, target))

