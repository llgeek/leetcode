class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            tmpres = []
            for sub in res:
                for j in range(len(sub) + 1):
                    tmpres.append(sub[:j] + [nums[i]] + sub[j:])
            res = tmpres[:]
        return res
