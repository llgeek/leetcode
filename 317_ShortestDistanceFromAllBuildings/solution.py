class Solution:
    def shortestDistance(self, grid):
        def helper(i, j):
            queue = [(i, j)]
            visited = {(i, j)}
            dist = 0
            direct = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while queue:
                nextlevel = []
                dist += 1
                while queue:
                    i, j = queue.pop()
                    for ii, jj in direct:
                        nebi, nebj = i + ii, j + jj
                        if nebi < 0 or nebi >= len(grid) or nebj < 0 or nebj >= len(grid[0]) \
                            or grid[nebi][nebj] == 2 or (nebi, nebj) in visited:
                            continue
                        visited.add((nebi, nebj))
                        nextlevel.append((nebi, nebj))
                        distances[nebi][nebj] += dist
                        reachable[nebi][nebj] += 1
                queue = nextlevel[:]

        if not grid or not any(grid):
            return -1
        m, n = len(grid), len(grid[0])
        INT_MAX = (1 << 31) - 1
        distances = [[0 for _ in range(n)] for _ in range(m)]
        reachable = [[0 for _ in range(n)] for _ in range(m)]

        building_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building_num += 1
                    helper(i, j)
        
        res = INT_MAX
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reachable[i][j] == building_num:
                    res = min(res, distances[i][j])
        return res if res != INT_MAX else -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    print(sol.shortestDistance(grid))
