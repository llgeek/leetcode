# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

class Solution:
    def validTree(self, n, edges):
        if not any(edges):
            return True
        ufhelper = UnionFind(n, edges)
        for edge in edges:
            if not ufhelper.union(edge[0], edge[1]):
                return False
        return ufhelper.count == 1



class UnionFind:
    def __init__(self, n, edges):
        self.parents = [-1] * n
        self.count = 0
        self.nodes = set()
        for edge in edges:
            if edge[0] not in self.nodes:
                self.count += 1
                self.parents[edge[0]] = edge[0]
                self.nodes.add(edge[0])
            if edge[1] not in self.nodes:
                self.count += 1
                self.parents[edge[1]] = edge[1]
                self.nodes.add(edge[1])


    def find(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        node1p = self.find(node1)
        node2p = self.find(node2)
        if node1p == node2p:
            return False
        self.parents[node2p] = node1p
        self.count -= 1
        return True


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    # edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    # edges = [[0, 1], [1, 2], [3, 4]]
    sol = Solution()
    print(sol.validTree(n, edges))
