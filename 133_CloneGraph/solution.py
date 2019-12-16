"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.cache = dict()
        def clone(node):
            if not node:
                return None
            if node.val in self.cache:
                return self.cache[node.val]
            newnode = Node(node.val, [])
            for neb in node.neighbors:
                newnode.neighbors.append(clone(neb))
            self.cache[node.val] = newnode
            return newnode
        
        return clone(node)
