"""
speed up by preprocessing the indexes in preorder
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
      
      def helper(instart, inend):
        if instart > inend: return None
        
        nonlocal pos
        root = TreeNode(preorder[pos])
        pos += 1
        root.left = helper(instart, val2idx[root.val] - 1)
        root.right = helper(val2idx[root.val] + 1, inend)
        return root

      if not preorder: return None
      val2idx = {val : idx for idx, val in enumerate(inorder)}
      pos = 0   # idx in preorder
      return helper(0, len(inorder) - 1)
