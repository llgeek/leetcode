"""
two level topological sorting
"""
from collections import deque, defaultdict
from typing import List
class ToplogicalGraph:
    def __init__(self):
        self.graph = defaultdict(lambda: set())
        self.in_degree = defaultdict(lambda: 0)
        self.out_degree = defaultdict(lambda: 0)

    def add_node(self, node):
        self.graph[node] = set()

    def add_edge(self, src, dst):
        self.graph[src].add(dst)
        self.in_degree[dst] += 1
        self.out_degree[src] += 1

    def sort(self):
        queue = deque()
        res = []
        for node in self.graph:
            if self.in_degree[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            result.append(node)
            for neb in self.graph[node]:
                self.in_degree[neb] -= 1
                if self.in_degree[neb] == 0:
                    queue.append(neb)
        return [] if len(res) < len(self.graph) else res

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group2item = defaultdict(lambda: [])
        mm = m
        for i in range(n):
            if group[i] == -1:
                group2item[mm].append(i)
                mm += 1
            else:
                group2item[group[i]].append(i)
        group_graph = ToplogicalGraph()
        for key, val in group2item.items():
            for 