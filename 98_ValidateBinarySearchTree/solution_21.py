# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.valid = True
        def helper(node, bound):
            if not node:
                return
            if not bound[0] < node.val < bound[1]:
                self.valid = False
                return
            if node.left:
                helper(node.left, (bound[0], node.val))
            if node.right:
                helper(node.right, (node.val, bound[1]))
        helper(root, (-float('inf'), float('inf')))
        return self.valid