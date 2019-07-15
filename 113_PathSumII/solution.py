from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: TreeNode, tsum: int) -> List[List[int]]:
        def dfs(node, path, val):
            if node.left:
                dfs(node.left, path + [node.val], val + node.val)
            if node.right:
                dfs(node.right, path + [node.val], val + node.val)
            if not node.left and not node.right and val + node.val == tsum:
                self.res.append(path + [node.val])
        if root:
            dfs(root, [], 0)   
        return self.res
