# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def helper(node):
            if node:
                self.res += 1
                if node.left:
                    helper(node.left)
                if node.right:
                    helper(node.right)
        
        self.res = 0
        helper(root)
        return self.res
