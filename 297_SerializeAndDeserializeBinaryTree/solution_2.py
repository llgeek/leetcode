# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SPLIT = "#"
    NULL = "*"

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return self.SPLIT.join(map(str, res))

    def serializeHelper(self, root, res):
        if not root:
            res.append(self.NULL)
            return
        res.append(root.val)
        self.serializeHelper(root.left, res)
        self.serializeHelper(root.right, res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(self.SPLIT))
        if not values:
          return None
        return self.deserializeHelper(values)
      
    def deserializeHelper(self, values):
        if not values:
          return
        curval = next(values)
        if curval == self.NULL:
          return None
        root = TreeNode(curval)
        root.left = self.deserializeHelper(values)
        root.right = self.deserializeHelper(values)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))