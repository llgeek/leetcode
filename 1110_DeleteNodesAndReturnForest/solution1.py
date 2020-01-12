# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        to_delete = set(to_delete)
        
        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete
            if not root_deleted and is_root:
                self.res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        
        helper(root, True)
        return self.res
