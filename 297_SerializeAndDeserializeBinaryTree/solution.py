# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SPLITER = ','
    NULL = 'X'
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        self.buildstring(root, ret)
        return ''.join(ret)

    def buildstring(self, node, ret):
        if not node:
            ret.extend([self.NULL, self.SPLITER])
        else:
            ret.extend([str(node.val), self.SPLITER])
            self.buildstring(node.left, ret)
            self.buildstring(node.right, ret)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(self.SPLITER)
        return self.buildtree(nodes)


    def buildtree(self, nodes):
        if not nodes:
            return None
        curval = nodes.pop(0)
        if curval == self.NULL:
            return None
        else:
            node = TreeNode(int(curval))
            node.left = self.buildtree(nodes)
            node.right = self.buildtree(nodes)
            return node


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))