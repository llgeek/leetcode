"""
recursive solution
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            self.res.append(root.val)
        helper(root)
        return self.res