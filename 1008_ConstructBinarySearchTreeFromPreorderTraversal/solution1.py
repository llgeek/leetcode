# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def preorderHelper(A, bound):
            if self.i == len(A) or A[self.i] >= bound:
                return None
            root = TreeNode(A[self.i])
            self.i += 1
            root.left = preorderHelper(A, root.val)
            root.right = preorderHelper(A, bound)
            return root

        self.i = 0
        MAXVAL = float('inf')
        return preorderHelper(preorder, MAXVAL)
