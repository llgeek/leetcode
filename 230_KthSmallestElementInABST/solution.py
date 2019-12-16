# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        def helper(root, k):
            if not root:
                return 0
            left = helper(root.left, k)
            if left + 1 == k:
                self.res = root.val
            right = helper(root.right, k-left-1)
            return left + right + 1
        helper(root, k)
        return self.res