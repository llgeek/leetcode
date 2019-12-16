# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, bound):
            if not root: return True
            if root.val <= bound[0] or root.val >= bound[1]:
                return False
            return helper(root.left, (bound[0], root.val)) and \
                    helper(root.right, (root.val, bound[1]))
        return helper(root, (-float('inf'), float('inf')))