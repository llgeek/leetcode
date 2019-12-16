# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        stack = [root]
        while stack:
            nextlevel = []
            thislevel = []
            while stack:
                node = stack.pop()
                thislevel.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            res.append(thislevel[:])
            stack = nextlevel[::-1]
        return res