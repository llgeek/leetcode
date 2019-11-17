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

        # return the vertex distance from root to target if exist, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(root):
            if not root:
                return -1
            if root is target:
                subtree_set(root, 0)
                return 1
            L, R = dfs(root.left), dfs(root.right)
            if L != -1:
                if L == K: 
                  self.ans.append(root.val)
                subtree_set(root.right, L + 1)
                return L + 1
            if R != -1:
                if R == K:
                    self.ans.append(root.val)
                subtree_set(root.left, R + 1)
                return R + 1
            return -1
              
        # Add all nodes 'K - dist' from the node to answer.
        def subtree_set(root, dist):
            if not root or dist > K: return 
            elif dist == K: self.ans.append(root.val)
            else:
                subtree_set(root.left, dist + 1)
                subtree_set(root.right, dist + 1)

        self.ans = []
        dfs(root)
        return self.ans