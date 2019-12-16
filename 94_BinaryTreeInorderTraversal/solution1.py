"""
iterative method
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curnode = root
        while stack or curnode:
            if curnode:
                stack.append(curnode)
                curnode = curnode.left
            curnode = stack.pop()
            res.append(curnode.val)
            curnode = curnode.right
        return res
