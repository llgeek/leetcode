# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = - 1 << 31
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(self.res, root.val, root.val + left, root.val + right, root.val + left + right)
            return max(0, root.val, root.val + right, root.val + left)
        helper(root)
        return self.res
            
        