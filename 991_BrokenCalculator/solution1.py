from collections import deque
class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        res = float('inf')
        tmp = 0
        if X == Y:
            return 0
        elif X > Y:
            return X - Y 
        else:
            while X < Y and not Y % 2:
                Y //= 2
                tmp += 1
            queue = deque()
            queue.append((X, 0))
            visited = {X}
            while queue:
                node, depth = queue.popleft()
                if node == Y:
                    res = min(res, tmp + depth)
                else:
                    if node-1 >= Y//2 and node-1 not in visited:
                        visited.add(node-1)
                        queue.append((node-1, depth+1))
                    if node < Y and node*2 not in visited:
                        visited.add(node*2)
                        queue.append((node*2, depth+1))
            return res

if __name__ == "__main__":
    X = 1
    Y = 1000000000
    sol = Solution()
    print(sol.brokenCalc(X, Y))
