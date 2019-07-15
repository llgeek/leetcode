"""
use Counter
"""
from typing import List
from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracker(ret, cnt, target, path, start):
            if target == 0:
                ret.append(path[:])
                return
            if start >= len(cnt): return

            else:
                backtracker(ret, cnt, target, path, start+1)

                val, num = cnt[start]
                maxtimes = min(target // val, num)
                for i in range(maxtimes):
                    path.append(val)
                    target -= val
                    backtracker(ret, cnt, target, path, start+1)
                for i in range(maxtimes):
                    path.pop()
                    target += val


        cnt = sorted(Counter(candidates).items(), key = lambda x: x[0])
        ret = []
        backtracker(ret, cnt, target, [], 0)
        return ret

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    # candidates = [2,5,2,1,2]
    target = 8
    # target = 5
    sol = Solution()
    print(sol.combinationSum2(candidates, target))