from collections import deque
class Solution:
    def minMutation(self, start: 'str', end: 'str', bank: 'List[str]') -> 'int':
        def buildGraph(bank):
            bankset = set(bank)
            graph = {}
            for node in bankset:
                if node not in graph:
                    graph[node] = set()
                for i in range(len(node)):
                    for c in 'ACGT':
                        if node[i] != c and node[:i] + c + node[i+1:] in bankset:
                            graph[node].add(node[:i] + c + node[i+1:])
                            if node[:i] + c + node[i+1:] not in graph:
                                graph[node[:i] + c + node[i+1:]] = {node}
                            else:
                                graph[node[:i] + c + node[i+1:]].add(node)
            del bankset
            return graph
        
        graph = buildGraph(bank + [start])
        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        while queue:
            node, depth = queue.popleft()
            if node == end:
                return depth
            elif node in graph:
                for nebnode in graph[node]:
                    if nebnode not in visited:
                        visited.add(nebnode)
                        queue.append((nebnode, depth+1))
        return -1
