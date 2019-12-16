from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(start, end):
            pre = (start, end)
            idx = 0
            while start + (1<<idx) <= end and nums[start + (1<<idx)] < target:
                idx += 1
            if idx:
                start += (1<<(idx-1))
            idx = 0
            while end - (1<<idx) >= start and nums[end - (1<<idx)] > target:
                idx += 1
            if idx:
                end -= (1<<(idx-1))
            if (start, end) == pre:
                return binary_search(start, end)
            else:
                return helper(start, end)
        def binary_search(start, end):
            if start > end: return [-1, -1]
            if start == end:
                return [start, end] if nums[start] == target else [-1, -1]
            left, right = start, end
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left_res = binary_search(start, mid -1) if start <= mid -1 else [-1, -1]
                    right_res = binary_search(mid + 1, end) if mid + 1 <= end else [-1, -1]
                    res = [mid, mid]
                    if left_res != [-1, -1]:
                        res[0] = left_res[0]
                    if right_res != [-1, -1]:
                        res[1] = right_res[1]
                    return res if res else [-1, -1]
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return [-1, -1]
        return helper(0, len(nums)-1)
                

if __name__ == "__main__":
    sol = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(sol.searchRange(nums, target))