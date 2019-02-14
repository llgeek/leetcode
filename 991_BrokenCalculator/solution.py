from collections import deque


class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        queue = deque()
        visited = set()
        # level = float('inf')
        queue.append((X, 0))
        visited.add(X)
        while queue:
            node, depth = queue.popleft()
            if node == Y:
                # if depth < level:
                return depth
            if 2*node > Y and node-1 not in visited:
                queue.append((node-1, depth+1))
                visited.add(node-1)
            if node < Y and node*2 not in visited:
                queue.append((node*2, depth+1))
                visited.add(node*2)
