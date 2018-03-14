class Solution:
    def longestConsecutive(self, root):
        """
        : type root: TreeNode
        : rtype: int
        """
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        maxlen = 1
        while stack:
            node, prelen = stack.pop()
            maxlen = max(maxlen, prelen)
            if node.left:
                nextlen = prelen + 1 if node.left.val == node.val + 1 else 1
                stack.append((node.left, nextlen))
            if node.right:
                nextlen = prelen + 1 if node.right.val == node.val + 1 else 1
                stack.append((node.right, nextlen))
        return maxlen
        

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    
def sampleTree():
    leaf1 = TreeNode(5, None, None)
    node2 = TreeNode(4, None, leaf1)
    leaf2 = TreeNode(2, None, None)
    node3 = TreeNode(3, leaf2, node2)
    node4 = TreeNode(1, None, node3)
    return node4

s = Solution()
root = sampleTree()
print(s.longestConsecutive(root))
