"""
remeber the parent of each node
then use DFS or BFS, it's just a graph

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, parent=None):
          """ remember the parent of each node
          """
          node.parent = parent
          if node.left: dfs(node.left, node)
          if node.right: dfs(node.right, node)
        
        dfs(root)
        seen = {target}
        
        # BFS
        from collections import deque
        queue = deque([(target, 0)])
        while queue:
            nextlevel = []
            if queue[0][1] == K:
                return [node[0].val for node in queue]
            while queue:
                node, dist = queue.popleft()
                for nei in {node.left, node.right, node.parent}:
                    if nei and nei not in seen:
                        seen.add(nei)
                        nextlevel.append((nei, dist+1))
            queue = deque(nextlevel)
        return []
              