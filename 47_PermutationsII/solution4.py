"""
use counter
"""

from typing import List
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtracker(ret, cnt, path):
            if len(path) == len(nums):
                ret.append(path[:])
            else:
                for val in cnt:
                    if cnt[val] > 0:
                        cnt[val] -= 1
                        backtracker(ret, cnt, path + [val])
                        cnt[val] += 1

        cnt = Counter(nums)
        ret = []
        backtracker(ret, cnt, [])
        return  ret

if __name__ == "__main__":
    nums = [1,1,2]
    # nums = [2,2,1,1]
    sol = Solution()
    print(sol.permuteUnique(nums))