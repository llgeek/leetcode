# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        i = 0
        while queue[i]:
          queue.append(queue[i].left)
          queue.append(queue[i].right)
          i += 1
        return not any(queue[i:])