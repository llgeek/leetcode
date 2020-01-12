from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def valid(target):
            acc, cnt = 0, 0
            for num in nums:
                acc += num
                if acc > target:
                    acc = num
                    cnt += 1
                if cnt > m:
                    return False
            if acc:
                cnt += 1
            return cnt <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    sol = Solution()
    nums = [7,2,5,10,8]
    m = 2
    print(sol.splitArray(nums, m))
