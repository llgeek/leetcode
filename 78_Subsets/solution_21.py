from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrakcer(res, tmpsub, startidx):
            res.append(tmpsub[:])
            for i in range(startidx, len(nums)):
                tmpsub.append(nums[i])
                backtrakcer(res, tmpsub, i+1)
                tmpsub.pop()
        res = []
        backtrakcer(res, [], 0)
        return res  

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.subsets(nums))
