from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(start, end):
            if start > end:
                return None 
            rootval = preorder[start]
            root = TreeNode(rootval)
            # idx = end+1
            idx = start + 1
            for idx in range(start+1, end+1):
                if preorder[idx] > rootval:
                    break
            if preorder[end] < rootval:
                root.left = helper(start+1, end)
            else:
                root.left = helper(start+1, idx-1)
                root.right = helper(idx, end)
            return root
        return helper(0, len(preorder)-1)
             