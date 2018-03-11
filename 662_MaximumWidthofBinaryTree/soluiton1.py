from collections import deque

"""
BFS implementations

"""
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodeque = deque()
        # store (node, level num, idx in that level in complete BST)
        nodeque.append((root, 0, 0))
        maxlen = 1
        curlev, leftidx, rightidx = -1, 0, 0
        preidx = 0
        while nodeque:
            node, level, idx = nodeque.popleft()
            if curlev != level:
                rightidx = preidx
                maxlen = max(maxlen, rightidx - leftidx + 1)
                curlev, leftidx  = level, idx
            if node.left:
                nodeque.append((node.left, level+1, idx*2))
            if node.right:
                nodeque.append((node.right, level+1, idx*2+1))
            preidx = idx
        return max(maxlen, preidx - leftidx+1)





