"""
iterator
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            tmpres = []
            for subres in res:
                tmpres.append(subres[:])
                tmpres.append(subres + [nums[i]])
            res = tmpres[:]
        return res
