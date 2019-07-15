"""
same as solution2.py
write in a more elegant way, avoid duplicate by avoid inserting dumplicate number after the same number

"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = [[]]
        for i in range(len(nums)):
            tmpret = []
            for sub in ret:
                for j in range(len(sub)+1):
                    tmpret.append(sub[:j] + [nums[i]] + sub[j:])
                    if j < len(sub) and nums[i] == sub[j]:
                        break
            ret = tmpret[:]
        return ret

if __name__ == "__main__":
    # nums = [1,1,2]
    nums = [2,2,1,1]
    sol = Solution()
    print(sol.permuteUnique(nums))