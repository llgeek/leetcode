# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node, depth):
            if not node: return
            if depth + 1 > self.res:
                self.res = depth + 1
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        helper(root, 0)
        return self.res
