# use dictionary, BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        rest = set()
        while stack:
            tmpstack = []
            for i in range(len(stack)):
                node = stack.pop()
                if k - node.val in rest: return True
                rest.add(node.val)
                if node.left: tmpstack.append(node.left)
                if node.right: tmpstack.append(node.right)
            stack = tmpstack[:]

        return False
        
        
        