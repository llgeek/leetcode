class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        ufhelper = UnionFind(equations)
        for equat in equations:
            if '==' in equat:
                ufhelper.union(equat[0], equat[-1])
        for equat in equations:
            if '!=' in equat:
                if ufhelper.find(equat[0]) == ufhelper.find(equat[-1]):
                    return False
        return True


class UnionFind:
    def __init__(self, equations):
        self.parent = dict()
        self.cnt = 0
        for equat in equations:
            if equat[0] not in self.parent:
                self.parent[equat[0]] = equat[0]
                self.cnt += 1
            if equat[-1] not in self.parent:
                self.parent[equat[-1]] = equat[-1]
                self.cnt += 1

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            self.parent[parent1] = parent2
            self.cnt -= 1

if __name__ == "__main__":
    equations = ["a==b", "b!=a"]
    # equations = ["b==a", "a==b"]
    # equations = ["a==b", "b==c", "a==c"]
    # equations = ["a==b", "b!=c", "c==a"]
    # equations = ["c==c", "b==d", "x!=z"]
    sol = Solution()
    print(sol.equationsPossible(equations))
