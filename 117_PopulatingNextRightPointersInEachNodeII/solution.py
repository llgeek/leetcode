"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = [root]
        while stack:
            nextlevel = []
            pre = None
            while stack:
                node = stack.pop()
                node.next = pre
                pre = node
                if node.right:
                    nextlevel.append(node.right)
                if node.left:
                    nextlevel.append(node.left)
            stack = nextlevel[::-1]
        return root
                