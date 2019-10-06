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
    nodes = [(root, 1)]
    i = 0
    while i < len(nodes):
      node, idx = nodes[i]
      if node:
        nodes.append((node.left, idx*2))
        nodes.append((node.right, idx*2+1))
      i += 1
    return nodes[-1][1] == len(nodes)