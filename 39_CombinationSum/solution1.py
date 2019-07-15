from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracker(ret, candidates, target, path, idx):
            if idx >= len(candidates):
                return
            if target == 0:
                ret.append(path[:])
            if candidates[idx] <= target:
                backtracker(ret, candidates, target, path, idx+1)        
                backtracker(ret, candidates, target-candidates[idx], path+[candidates[idx]], idx)
        candidates.sort()
        ret = []
        backtracker(ret, candidates, target, [], 0)
        return ret

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))