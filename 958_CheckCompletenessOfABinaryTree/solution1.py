# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import List
class Solution:
  def isCompleteTree(self, root: TreeNode) -> bool:
    queue = deque([root])
    end = False
    while queue:
      node = queue.popleft()
      if not node: 
        end = True
      else:
        if end: return False
        queue.append(node.left)
        queue.append(node.right)
    return True


