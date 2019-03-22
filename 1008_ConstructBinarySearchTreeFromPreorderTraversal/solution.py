# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(start, end):
            rootval = preorder[start]
            root = TreeNode(rootval)
            idx = start + 1
            while idx <= end and preorder[idx] < rootval:
                idx += 1
            if idx != start + 1:
                root.left = helper(start+1, idx-1)
            if idx <= end:
                root.right = helper(idx, end)
            return root

        return helper(0, len(preorder)-1)
