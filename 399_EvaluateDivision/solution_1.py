"""
union find
"""
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ufhelper = UnionFind(equations)
        for eqt, val in zip(equations, values):
            ufhelper.union(eqt, val)
        res = []
        for query in queries:
            if not ufhelper.exist(query):
                res.append(-1.)
                continue
            q1 = ufhelper.find(query[0])
            q2 = ufhelper.find(query[1])
            if q1[0] != q2[0]:
                res.append(-1.)
            else:
                res.append(q1[1] / q2[1])
        return res

class UnionFind():
    def __init__(self, equations):
        self.parent = {}
        for eqt in equations:
            self.parent[eqt[0]] = (eqt[0], 1.0)
            self.parent[eqt[1]] = (eqt[1], 1.0)

    def exist(self, pair):
        return pair[0] in self.parent and pair[1] in self.parent

    def find(self, c):
        if c == self.parent[c][0]:
            return self.parent[c]
        val = 1.0
        p = c
        while p != self.parent[p][0]:
            p, _val = self.find(self.parent[c][0])
            self.parent[c] = (p, _val * self.parent[c][1])
        return self.parent[c]

    def union(self, pair, val):
        p1 = self.find(pair[0])
        p2 = self.find(pair[1])
        self.parent[p1[0]] = (p2[0], val * p2[1] / p1[1])

if __name__ == "__main__":
    sol = Solution()
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    print(sol.calcEquation(equations, values, queries))