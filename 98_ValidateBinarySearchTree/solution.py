# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def helper(node, lower, higher):
            if not node:
                return True
            if lower is not None and lower >= node.val:
                return False
            if higher is not None and higher <= node.val:
                return False
            left = helper(node.left, lower, node.val) if node.left else True
            if left:
                right = helper(node.right, node.val, higher) if node.right else True
                return right
            else:
                return False
            
        return helper(root, None, None)

