# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:
    SPLITER = '#'
    NULL = 'X'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            res = []
            if root:
                res.append(str(root.val))
                left = helper(root.left)
                right = helper(root.right)
                res.extend(left)
                res.extend(right)
            else:
                res.append(self.NULL)
            return res
        res = helper(root)
        return self.SPLITER.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(nodelist):
            val = nodelist.popleft()
            if val == self.NULL:
                return None
            else:
                root = TreeNode(int(val))
                root.left = helper(nodelist)
                root.right = helper(nodelist)
                return root

        if not data:
            return None
        nodelist = deque(data.split(self.SPLITER))
        return helper(nodelist)









# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
