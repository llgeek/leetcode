from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        pos = defaultdict(lambda: [])
        queue = deque([(root, 0)])
        while queue:
          nextlevel = deque([])
          levelpos = defaultdict(lambda: [])
          while queue:
            node, idx = queue.popleft()
            if node.left:
              nextlevel.append((node.left, idx-1))
            if node.right:
              nextlevel.append((node.right, idx+1))
            levelpos[idx] += [node.val]
          queue = nextlevel.copy()
          for idx in levelpos.keys():
            pos[idx] += sorted(levelpos[idx])
        return [pos[idx] for idx in sorted(pos.keys())]