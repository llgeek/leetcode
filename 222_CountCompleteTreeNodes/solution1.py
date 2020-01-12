# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(node):
            return -1 if not node else 1 + height(node.left)
        
        h = height(root)
        if h == -1:
            return 0
        rh = height(root.right)
        return (1 << h) + self.countNodes(root.right) if rh == h - 1 else (1 << (h - 1)) + self.countNodes(root.left)