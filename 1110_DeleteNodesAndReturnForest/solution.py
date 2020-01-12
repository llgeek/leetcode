# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        to_delete = set(to_delete)
        def helper(node, first=True):
            if not node:
                return
            if first and node.val not in to_delete:
                self.res.append(node)
            helper(node.left, node.val in to_delete)
            helper(node.right, node.val in to_delete)
            if node.left and node.left.val in to_delete:
                node.left = None
            if node.right and node.right.val in to_delete:
                node.right = None
        helper(root, True)
        return self.res