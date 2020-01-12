"""
BFS
"""
from typing import List
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        def add_edge(s, t, v):
            graph[s] = graph.get(s, []) + [(t, v)]
        def build_graph():
            for eqt, val in zip(equations, values):
                add_edge(*eqt, val)
                add_edge(*eqt[::-1], 1. / val)

        def find_path(s, t):
            if s not in graph or t not in graph:
                return -1.
            visited = set()
            queue = deque([(s, 1.0)])
            while queue:
                v, w = queue.popleft()
                visited.add(v)
                if v == t:
                    return w
                for neb, nebw in graph[v]:
                    if neb not in visited:
                        queue.append((neb, w * nebw))
            return -1.

        build_graph()
        res = []
        for query in queries:
            w = find_path(*query)
            if w != -1.:
                add_edge(*query, w)
                add_edge(*query[::-1], 1. / w)
            res.append(w)
        return res

                
