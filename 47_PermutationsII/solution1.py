"""
backtracker nums, swap nums directly

use set 
"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracker(ret, nums, begin):
            if begin >= len(nums):
                ret.append(nums[:])
            else:
                appeared = set()
                for i in range(begin, len(nums)):
                    if nums[i] not in appeared:
                        appeared.add(nums[i])
                        nums[i], nums[begin] = nums[begin], nums[i]
                        backtracker(ret, nums, begin+1)
                        nums[i], nums[begin] = nums[begin], nums[i]

        nums.sort()
        ret = []
        backtracker(ret, nums, 0)
        return ret

if __name__ == "__main__":
    # nums = [1,1,2]
    # nums = [2,2,1,1]
    nums = [0,1,0,0,9]
    sol = Solution()
    print(sol.permuteUnique(nums))
