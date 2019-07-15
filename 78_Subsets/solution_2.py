from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for val in nums:
            res += [sub + [val] for sub in res]
        return res  

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.subsets(nums))