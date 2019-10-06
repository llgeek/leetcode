from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(preorder, bound):
            if self.idx >= len(preorder) or preorder[self.idx] > bound:
                return None 
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(preorder, root.val)
            root.right = helper(preorder, bound)
            return root
        
        self.idx = 0
        MAXVAL = (1<<31)-1
        return helper(preorder, MAXVAL)
