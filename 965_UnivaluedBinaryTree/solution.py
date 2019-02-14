# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left:
            if not self.isUnivalTree(root.left) or (self.isUnivalTree(root.left) and root.val != root.left.val):
                return False
        if root.right:
            if not self.isUnivalTree(root.right) or (self.isUnivalTree(root.right) and root.val != root.right.val):
                return False
        return True