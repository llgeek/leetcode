from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        p1, p2, p3 = 0, 0, 0
        c1, c2, c3 = 0, 0, 0
        pre = - 1 << 31
        i = 0
        while i < len(nums):
            cnt = 1
            cur = nums[i]
            while i + 1 < len(nums) and nums[i+1] == cur:
                i += 1
                cnt += 1
            if cur != pre + 1:
                if p1 != 0 or p2 != 0:
                    return False
                c1 = cnt
                c2 = 0
                c3 = 0
            else:
                if cnt < p1 + p2:
                    return False
                c2 = p1
                c3 = p2 + min(p3, cnt - p1 - p2)
                c1 = max(cnt - p1 - p2 - p3, 0)
            p1 = c1
            p2 = c2
            p3 = c3
            pre = cur
            i += 1
        return p1 == p2 == 0

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,3,4,5]
    # [1,2,3,3,4,4,5,5]
    print(sol.isPossible(nums))