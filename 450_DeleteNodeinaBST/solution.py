# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def findAncestor(root, node):

        if root.val == key:
        curnode = root
        parent = None
        while curnode:
            if key < curnode.val:
                curnode = curnode.left
                parent = curnode
            if key > rocurnodeot.val:
                curnode = curnode.right
                parent = curnode
            if key == curnode.val: 
                if not 
