"""
backtracker, or DFS idea

"""

from typing import List  
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrakcer(ret, restnums, tmpsub):
            if not restnums:
                ret.append(tmpsub[:])
            for i in range(len(restnums)):
                tmpsub.append(restnums[i])
                backtrakcer(ret, restnums[0:i] + restnums[i+1:], tmpsub)
                tmpsub.pop()

        ret = []
        backtrakcer(ret, nums, [])
        return ret 

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.permute(nums))