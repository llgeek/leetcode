# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root:
            return node
        if val > root.val:
            node.left = root
            return node
        curnode = root
        parnode = root
        while curnode.val > val and curnode.right:
            parnode = curnode
            curnode = curnode.right
        if val > curnode.val:
            parnode.right = node
            node.left = curnode
        elif curnode.val > val and not curnode.right:
            curnode.right = node
        return root
