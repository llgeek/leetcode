# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
          if not root.left and not root.right:
            return root, root
          L, R = None, None
          if root.left:
            L, llast = helper(root.left)
          if root.right:
            R, rlast = helper(root.right)
          if L and R:
            root.right = L
            root.left = None
            llast.left = None
            llast.right = R
            return root, rlast
          elif L:
            root.left = None
            root.right = L
            return root, llast
          else:
            root.left = None
            root.right = R
            return root, rlast
        helper(root)[0]



          