"""
DFS, element by element visit
"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = [([],-1)]
        for i in range(len(nums)):
            tmpret = []
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                for sub, _ in ret:
                    for j in range(len(sub)+1):
                        tmpret.append((sub[:j] + [nums[i]] + sub[j:], j))
            else:
                for sub, preidx in ret:
                    for j in range(preidx+1, len(sub)+1):
                        tmpret.append((sub[:j] + [nums[i]] + sub[j:], j))
            ret = tmpret[:]
        return [sub for sub, _ in ret]

if __name__ == "__main__":
    # nums = [1,1,2]
    nums = [2,2,1,1]
    sol = Solution()
    print(sol.permuteUnique(nums))