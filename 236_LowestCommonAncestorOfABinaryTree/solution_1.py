# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None, -1
        def helper(node, depth):
            if not node:
                return 0
            val = helper(node.left, depth+1) + helper(node.right, depth+1) + (node == p or node == q)
            if val == 2 and depth > self.ans[1]:
                self.ans = node, depth
            return val
        helper(root, 0)
        return self.ans[0]

          