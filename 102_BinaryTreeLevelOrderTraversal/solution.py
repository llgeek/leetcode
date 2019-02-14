# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        from collections import deque
        ret = []
        if not root:
            return ret
        queue = deque()
        queue.append((root, 0))
        prelev = 0
        levval = []
        while queue:
            node, curlev = queue.popleft()
            if curlev != prelev:
                ret.append(levval.copy())
                levval = []
                prelev = curlev
            levval.append(node.val)
            if node.left:
                queue.append((node.left, curlev+1))
            if node.right:
                queue.append((node.right, curlev+1))
        if levval:
            ret.append(levval)
        return ret


