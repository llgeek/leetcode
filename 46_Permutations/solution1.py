"""
very elegant solution

instead of backtrack tmpsolution, backtracker to swap elements in original nums list

"""

from typing import List  
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracker(ret, nums, begin):
            if begin >= len(nums):
                ret.append(nums[:])
            else:
                for i in range(begin, len(nums)):
                    nums[i], nums[begin] = nums[begin], nums[i]
                    backtracker(ret, nums, begin+1)
                    nums[i], nums[begin] = nums[begin], nums[i]
        ret = []
        backtracker(ret, nums, 0)
        return ret  

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.permute(nums))