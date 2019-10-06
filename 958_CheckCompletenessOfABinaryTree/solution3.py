"""
DFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from collections import deque
from typing import List
class Solution:
  def isCompleteTree(self, root: TreeNode) -> bool:
    def dfs(node, coord):
      if not node:
        return 0, 0
      left = dfs(node.left, coord*2)
      right = dfs(node.right, coord*2+1)
      tot = 1 + left[0] + right[0]
      coord = max(coord, left[1], right[1])
      return tot, coord
    if not root: return True
    tot, coord = dfs(root, 1)
    return tot == coord