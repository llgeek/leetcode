class Solution:
    def knightMoves(self, x, y):
        x, y = abs(x), abs(y)
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        visited = set()
        queue = [(0, 0)]
        # visited.add((0, 0))
        step = 0
        while queue:
            nextlevel = []
            step += 1
            while queue:
                i, j = queue.pop()
                visited.add((i, j))
                for xx, yy in zip(dx, dy):
                    nebi, nebj = i + xx, j + yy
                    if nebi == x and nebj == y:
                        return step
                    if nebi < 0 or nebi > x or nebj < 0 or nebj > y or (nebi, nebj) in visited:
                        continue
                    nextlevel.append((nebi, nebj))
            queue = nextlevel[:]
        return -1

if __name__ == "__main__":
    sol = Solution()
    x = 200
    y = 100
    print(sol.knightMoves(x, y))
