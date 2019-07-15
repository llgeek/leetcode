"""
backtracker
"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracker(ret, restnums, tmpsub):
            if not restnums:
                ret.append(tmpsub[:])
            else:
                for i in range(len(restnums)):
                    if i == 0 or restnums[i] != restnums[i-1]:
                        tmpsub.append(restnums[i])
                        backtracker(ret, restnums[:i] + restnums[i+1:], tmpsub)
                        tmpsub.pop()
        nums.sort()
        ret = []
        backtracker(ret, nums, [])
        return  ret  

if __name__ == "__main__":
    nums = [1,1,2]
    sol = Solution()
    print(sol.permuteUnique(nums))
        
        