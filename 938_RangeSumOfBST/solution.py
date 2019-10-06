# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def recursive(node, L, R):
          if not node: return 0
          if node.val <= L: return recursive(node.right, L, R) + (node.val if node.val == L else 0)
          if node.val >= R: return recursive(node.left, L, R) + (node.val if node.val == R else 0)
          return node.val + recursive(node.left, L, node.val) + recursive(node.right, node.val, R)
        return recursive(root, L, R)
          
