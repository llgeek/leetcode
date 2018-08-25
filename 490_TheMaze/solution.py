class Solution:
    def hasPath(self, maze, start, destination):
        if not maze or not maze[0]:
            return False
        self.m, self.n = len(maze), len(maze[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        return self.DFS(maze, start, destination, self.visited)

    
    def DFS(self, maze, curidx, destination, visited):
        x, y = curidx
        if self.visited[x][y]:
            return False
        if curidx == destination:
            return True
        self.visited[x][y] = True
        tx, ty = x, y
        while x - 1 >= 0 and not maze[x - 1][y]:
            x -= 1
        if self.DFS(maze, (x, y), destination, self.visited):
            return True
        x, y = tx, ty
        while x + 1 < self.m and not maze[x + 1][y]:
            x += 1
        if self.DFS(maze, (x, y), destination, self.visited):
            return True
        x, y = tx, ty
        while y - 1 >= 0 and not maze[x][y-1]:
            y -= 1
        if self.DFS(maze, (x, y), destination, self.visited):
            return True
        x, y = tx, ty
        while y + 1 < self.n and not maze[x][y+1]:
            y += 1
        if self.DFS(maze, (x, y), destination, self.visited):
            return True
        return False
            

s = Solution()
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

canmaze = [[0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]
#print(s.hasPath(maze, (0, 4), (3, 2)))
#print(s.hasPath(canmaze, (0,4), (4,4)))
print(s.hasPath(maze, (0, 4), (4,4)))
