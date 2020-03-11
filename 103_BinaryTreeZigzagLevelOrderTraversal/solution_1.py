# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        rev = False
        while stack:
            nextlevel = []
            curlevel = []
            while stack:
                node = stack.pop()
                curlevel.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            stack = nextlevel[::-1]
            res.append(curlevel[:] if not rev else curlevel[::-1])
            rev = not rev
        return res
