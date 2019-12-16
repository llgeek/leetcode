from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        def helper(idx, remain, path=[]):
            if idx >= len(candidates):
                # if remain == 0:
                #     self.res.append(path)
                # else:
                return
            if candidates[idx] > remain:
                return
            elif candidates[idx] == remain:
                self.res.append(path + [candidates[idx]])
                return
            else:
                helper(idx+1, remain, path)
                helper(idx, remain-candidates[idx], path+[candidates[idx]])
        helper(0, target, [])
        return self.res

if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(sol.combinationSum(candidates, target))