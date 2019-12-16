# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if left < right - 1 or right < left - 1:
                self.balanced = False
            return 1 + max(left, right)
        helper(root)
        return self.balanced