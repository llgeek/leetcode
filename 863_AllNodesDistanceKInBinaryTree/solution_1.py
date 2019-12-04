"""
idea: build a graph, then start from target, use bfs to get all nodes with distance K
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
  def distanceK(self, root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    if not root: return []
    def helper(node, parent):
      if node:
        node.next = parent
        if node.left:
          helper(node.left, node)
        if node.right:
          helper(node.right, node)
    helper(root, None)

    queue = [(target, 0)]
    visited = {target}
    res = []
    while queue:
      node, dist = queue.pop()
      if dist > K:
        continue
      if dist == K:
        res.append(node.val)
        continue
      for neb in {node.left, node.right, node.parent}:
        if neb and neb not in visited:
          visited.add(neb)
          queue.append((neb, dist+1))
    return res

