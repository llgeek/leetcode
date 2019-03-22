"""
not finished
"""

import itertools
# class Solution:
#     def judgePoint24(self, nums) -> bool:
#         def dfs(vals, candidates):
#             if not candidates:
#                 return any(abs(val - 24) < 1e-6 for val in vals)
#             res = False
#             for i, curnum in enumerate(candidates):
#                 nextvals = []
#                 nextcandidates = candidates[:i] + candidates[i+1:]
#                 for val in vals:
#                     nextvals += [val + curnum, val-curnum, curnum-val, val*curnum, val/curnum if curnum != 0 else val/1e-6, curnum/val if val != 0 else curnum/1e-6]
#                     res |= dfs(set(nextvals), nextcandidates)
#             return res

#         return any(dfs({a+b, a-b, b-a, a*b, a/b if b !=0 else a/1e-6, b/a if a!=0 else b/1e-6}, [c,d]) for a,b,c,d in itertools.permutations(nums))


class Solution:
    OP = {'+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: x/y}
    def judgePoint24(self, nums) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    nextnums = [val for k, val in enumerate(nums) if k != i and k != j]
                    for op in self.OP:
                        if op != '/' or nums[j]:
                            if self.judgePoint24(nextnums+[self.OP[op](nums[i], nums[j])]):
                                return True
        return False


if __name__ == "__main__":
    # nums = [4, 1, 8, 7]
    # nums = [1, 2, 1, 2]
    nums = [1,9,1, 2]
    sol = Solution()
    print(sol.judgePoint24(nums))

                
