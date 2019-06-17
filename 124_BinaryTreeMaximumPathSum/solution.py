# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxValDown(root):
            if not root:
                return 0
            left = max(0, maxValDown(root.left))
            right = max(0, maxValDown(root.right))
            self.maxsum = max(self.maxsum, left+right+root.val)
            return max(left, right) + root.val

        self.maxsum = -float('inf')
        maxValDown(root)
        return self.maxsum