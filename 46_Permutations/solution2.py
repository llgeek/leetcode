"""
another non backtrack solution

visit each element and insert into each possible position
"""

from typing import List  
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for val in nums:
            tmpret = []
            for sub in ret:
                for j in range(len(sub)+1):
                    tmpret.append(sub[:j] + [val] + sub[j:])
            ret = tmpret[:]
        return ret  

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.permute(nums))
