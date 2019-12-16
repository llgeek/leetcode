# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        stack = [root]
        rev = True
        while stack:
            nextlevel = []
            res.append([])
            while stack:
                node = stack.pop()
                res[-1].append(node.val)
                if rev:
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                else:
                    if node.right:
                        nextlevel.append(node.right)
                    if node.left:
                        nextlevel.append(node.left)
            rev = not rev
            stack = nextlevel[:]
        return res
                
