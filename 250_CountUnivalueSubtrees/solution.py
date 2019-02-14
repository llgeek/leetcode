

# Definition for singly-linked list.
# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():
    def countUnivalueSubtree(self, root):
        def recursivehelper(root):
            if not root:
                return 0, True, None
            if not root.left and not root.right:
                return 1, True, root.val
            leftcnt, leftbool, leftval, rightcnt, rightbool, rightval = 0, None, None, 0, None, None
            if root.left:
                leftcnt, leftbool, leftval = recursivehelper(root.left)
            if root.right:
                rightcnt, rightbool, rightval = recursivehelper(root.right)
            if leftbool == False or rightbool == False:
                return leftcnt+rightcnt, False, root.val
            if leftval == rightval == root.val:
                return leftcnt+rightcnt+1, True, root.val
            else:
                return leftcnt+rightcnt, False, root.val

        cnt, _, _ = recursivehelper(root)
        return cnt

