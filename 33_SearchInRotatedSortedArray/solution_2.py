from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        pivot = 0
        # wrong! it's not O(logn), it's O(n)
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         pivot = i
        #         break
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        realidx = lambda idx: (idx + pivot) % len(nums)
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = begin + (end - begin) // 2
            if nums[realidx(mid)] == target:
                return realidx(mid)
            elif nums[realidx(mid)] < target:
                begin = mid + 1
            else:
                end = mid - 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 3]
    # target = 1  
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(sol.search(nums, target))
