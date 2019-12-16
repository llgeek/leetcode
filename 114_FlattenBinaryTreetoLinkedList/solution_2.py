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
            if not root: return None, None
            if not root.left and not root.right:
                return root, root
            lefthead, righthead = None, None
            if root.right:
                righthead, righttail = helper(root.right)
            if root.left:
                lefthead, lefttail = helper(root.left)
            if lefthead and righthead:
                root.left = None
                root.right = lefthead
                lefttail.left = None
                lefttail.right = righthead
                righthead.left = None
                return root, righttail
            elif lefthead:
                root.left = None
                root.right = lefthead
                return root, lefttail
            elif righthead:
                root.left = None
                root.right = righthead
                return root, righttail
        return helper(root)