"""
recursive way

backtrack

O(n) time complexity
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recursiveTree(root):
            if not root:
                return False
            left = recursiveTree(root.left)
            mid = root == p or root == q
            right = recursiveTree(root.right)
            if left + mid + right >= 2:
                self.ans = root
            return left or mid or right
        self.ans = None
        recursiveTree(root)
        return self.ans

    