"""
optimize the complexity

use phthon's defaultdict

BFS idea, level by leve, so that each time we consider the same height/ y value
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        pos = defaultdict(list)
        queue = [root, 0]
        while queue:    #BFS
            nextqueue = []
            tmp = defaultdict(list)     # res at the same level/ y value
            while queue:
                node, x = queue.pop()
                tmp[x].append(node.val)
                if node.left: nextqueue.append((node.left, x-1))
                if node.right: nextqueue.append((node.right, x+1))
            # x is the x axis, put all list to the same y index as y is the same at this level
            for x in tmp:
                pos[x].extend(sorted(tmp[x]))
            queue = nextqueue
        return [pos[x] for x in sorted(pos)]
