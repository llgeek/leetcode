"""
第一轮:给一棵树(不一定是二叉树)和一个节点(保证存在),按层次遍历顺序查询该节点的上一个节点,每层第一个 节点的上一个节点规定为NULL。
Follow up1:经常查询的话如何优化.
Follow up2:给定父节点,如何支持插入操作

Page 2
"""

from collections import deque
class Solution:
    def treeSearch(self, root, target):
        """
        type root: TreeNode
        rtype: TreeNode
        """
        if not root:
            return None
        nodeque = deque()
        nodeque.append(root)
        while nodeque:
            prenode = None
            num = len(nodeque)
            while num:
                num -= 1
                curnode = nodeque.popleft()
                if curnode == target:
                    return prenode
                prenode = curnode
                for node in curnode.child:      #Pseudo code
                    nodeque.append(node)
        return None


"""
follow up 1
using map to store each node's previous node
"""
    def treeSearchBuildMap(self, root):
        if not root:
            return None
        self.node2prenode = dict{}
        nodeque = deque()
        nodeque.append(root)
        while nodeque:
            prenode = None
            num = len(nodeque)
            while num:
                num -= 1
                curnode = nodeque.popleft()
                self.node2prenode[curnode] = prenode
                prenode = curnode
                for node in curnode.child:      # Pseudo code
                    nodeque.append(node)

    def treeSearchMap(self, root, target):
        self.treeSearchBuildMap(root)
        return self.node2prenode[target]
        #return self.node2prenode.get(target, None)     //if the target node is not ensured to be existed







