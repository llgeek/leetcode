# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        level = 0
        while queue:
            nextlevel = []
            level += 1
            while queue:
                node = queue.pop()
                if not node.left and not node.right:
                    return level
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            queue = nextlevel[:]
        return level
