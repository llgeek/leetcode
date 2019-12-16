# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preidx = 0
        def helper(sidx, eidx):
            if sidx > eidx:
                return None
            root = TreeNode(preorder[self.preidx])
            self.preidx += 1
            i = sidx
            while i <= eidx:
                if inorder[i] == root.val:
                    break
                i += 1
            root.left = helper(sidx, i-1)
            root.right = helper(i+1, eidx)
            return root
        return helper(0, len(inorder)-1)