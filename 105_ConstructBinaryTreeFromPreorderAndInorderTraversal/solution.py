# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(prestart, instart, inend):
          if prestart > len(preorder) - 1 or instart > inend:
            return None
          root = TreeNode(preorder[prestart])
          inidx = 0
          for inidx in range(instart, inend + 1):
            if inorder[inidx] == preorder[prestart]:
              break
          root.left = helper(prestart+1, instart, inidx - 1)
          root.right = helper(prestart + inidx - instart + 1, inidx + 1, inend)
          return root
        
        return helper(0, 0, len(inorder)-1)
          
