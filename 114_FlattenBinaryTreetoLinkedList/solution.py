# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flatten_helper(node):
            left = node.left
            right = node.right
            if not left and not right:
                return node
            elif not left and right:
                return flatten_helper(right)
            elif not right and left:
                node.right = left
                node.left = None
                return flatten_helper(left)
            else:
                node.right = left
                node.left = None
                lastnode = flatten_helper(left)
                lastnode.left = None
                lastnode.right = right
                return flatten_helper(right)
        if not root:
            return
        flatten_helper(root)
        
    
