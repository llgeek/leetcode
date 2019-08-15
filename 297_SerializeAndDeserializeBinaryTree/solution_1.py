# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    NULL = 'N'
    SPLIT = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        self.encode(root, ret)
        return self.SPLIT.join(ret)

    def encode(self, node, ret):
        if not node:
            ret.append(self.NULL)
        else:
            cur = str(node.val)
            ret.append(cur)
            self.encode(node.left, ret)
            self.encode(node.right, ret)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vallist = data.split(self.SPLIT)
        return self.decode(vallist)

    def decode(self, vallist):
        curval = vallist.pop(0)
        if curval == self.NULL:
            return None
        else:
            node = TreeNode(int(curval))
            node.left = self.decode(vallist)
            node.right = self.decode(vallist)
            return node

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))