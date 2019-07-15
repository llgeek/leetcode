from typing import List
from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracker(res, tmpsub, cnt, startidx):
            res.append(tmpsub[:])
            for i in range(startidx, len(cnt)):
                for j in range(cnt[i][1]):
                    tmpsub.append(cnt[i][0])
                    backtracker(res, tmpsub, cnt, i+1)
                for j in range(cnt[i][1]):
                    tmpsub.pop()
        cnt = Counter(nums).most_common()
        res = []
        backtracker(res, [], cnt, 0)
        return res

if __name__ == "__main__":
    nums = [1,2,2]
    sol = Solution()
    print(sol.subsetsWithDup(nums))
