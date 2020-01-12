from typing import List
class Node:
    def __init__(self, val, s):
        self.val = val
        self.dup = 0
        self.sum = s
        self.left = None
        self.right = None

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        root = None
        res = [None] * len(nums)
        



# from typing import List
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return []
#         nextsmall = [-1] * len(nums)
#         stack = []
#         for i, v in enumerate(nums):
#             while stack and stack[-1][0] > v:
#                 pv, pi = stack.pop()
#                 nextsmall[pi] = i
#             stack.append((v, i))
        
#         self.res = [None] * len(nums)
#         def helper(pos):
#             if self.res[pos] == None:
#                 if nextsmall[pos] == -1:
#                     self.res[pos] = 0
#                 else:
#                     self.res[pos] = helper(nextsmall[pos]) + 1
#             return self.res[pos]
#         for i in range(len(nums)):
#             if self.res[i] == None:
#                 helper(i)
#         return self.res

if __name__ == "__main__":
    sol = Solution()
    nums = [5,2,6,1]
    print(sol.countSmaller(nums))
