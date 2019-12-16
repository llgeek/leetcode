# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> bool:
        res = []
        if not root: return False
        stack = [(root, 0, [])]
        while stack:
            node, pathval, path = stack.pop()
            if node.left:
                stack.append((node.left, pathval + node.val, path + [node.val]))
            if node.right:
                stack.append((node.right, node.val + pathval, path + [node.val]))
            if not node.left and not node.right and pathval + node.val == sum:
                res.append(path + [node.val])
        return res


        