from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.idx = 0
        self.maxval = (1<<31)-1
        def helper(val):
          if self.idx >= len(preorder) or preorder[self.idx] > val:
            return None
          root = TreeNode(preorder[self.idx])
          self.idx += 1
          root.left = helper(root.val)
          root.right = helper(val)
          return root
        return helper(self.maxval)


if __name__ == "__main__":
    sol = Solution()
    preorder = [8,5,1,7,10,12]
    root = sol.bstFromPreorder(preorder)