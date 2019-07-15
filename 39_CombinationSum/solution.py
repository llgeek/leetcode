from typing import List  
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracker(ret, candidates, target, path, start):
            if 0 < start < len(candidates) and candidates[start] == candidates[start-1] or start >= len(candidates):
                return
            if target == 0:
                ret.append(path[:])
            else:
                for i in range(start, len(candidates)):
                    if candidates[i] <= target:
                        path.append(candidates[i])
                        backtracker(ret, candidates, target-candidates[i], path, i)
                        path.pop()
                    else:
                        break
        candidates.sort()
        ret = []
        backtracker(ret, candidates, target, [], 0)
        return ret

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))