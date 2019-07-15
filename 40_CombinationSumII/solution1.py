from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracker(ret, candidates, target, path, start):
            if target < 0:
                return
            if target == 0:
                ret.append(path[:])
            else:
                for i in range(start, len(candidates)):
                    if i != start and candidates[i] == candidates[i-1]:
                        continue
                    if candidates[i] <= target:
                        path.append(candidates[i])
                        backtracker(ret, candidates, target-candidates[i], path, i+1)
                        path.pop()
                    else:
                        break

        candidates.sort()     
        ret = []
        backtracker(ret, candidates, target, [], 0)
        return ret

if __name__ == "__main__":
    # candidates = [10,1,2,7,6,1,5]
    # candidates = [2,5,2,1,2]
    # target = 8
    # target = 5
    candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
    target = 27
    sol = Solution()
    print(sol.combinationSum2(candidates, target))