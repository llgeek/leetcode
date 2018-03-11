"""
DFS implementation
"""
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftidx = dict()
        nodestack = []
        nodestack.append((root, 0, 0))
        maxlen = 0
        while nodestack:
            node, level, idx = nodestack.pop()
            if node:
                leftidx.setdefault(level, idx)
                maxlen = max(maxlen, idx - leftidx[level]+1)
                nodestack.append((node.right, level+1, idx*2+1))
                nodestack.append((node.left, level+1, idx*2))
        return maxlen