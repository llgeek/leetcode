"""
Leetcode 490

https://leetcode.com/articles/the-maze/
"""
from collections import deque
class Solution:
    def hasPath(self, maze, start, destination):
        self.visited = [[False for _ in range(len(maze[0]))] for __ in range(len(maze))]
        self.m = len(maze)
        self.n = len(maze)
        #return self.dfs(maze, start, destination)

        self.nodeque = deque()
        self.nodeque.append(start)
        return self.bfs(maze, start, destination)

        


    def dfs(self, maze, start, destination):
        if self.visited[start[0]][start[1]]:
            return False
        if start == destination:
            return True
        self.visited[start[0]][start[1]] = True
        l, r, u, d = start[1]-1, start[1]+1, start[0]-1, start[0]+1
        while l >= 0 and not maze[start[0]][l]:
            l -= 1
        if self.dfs(maze, (start[0], l+1), destination):
            return True
        while r < self.n and not maze[start[0]][r]:
            r += 1
        if self.dfs(maze, (start[0], r-1), destination):
            return True
        while u >= 0 and not maze[u][start[1]]:
            u -= 1
        if self.dfs(maze, (u+1, start[1]), destination):
            return True
        while d < self.m and not maze[d][start[1]]:
            d += 1
        if self.dfs(maze, (d-1, start[1]), destination):
            return True
        #self.visited[start[0]][start[1]] = False
        return False

    # def bfs(self, maze, start, destination):
    #     while self.nodeque:
    #         num = len(self.nodeque)
    #         while num:
    #             curpos = self.nodeque.popleft()
    #             num -= 1
    #             if self.visited[curpos[0]][curpos[1]]:
    #                 continue
    #             else:
    #                 self.visited[curpos[0]][curpos[1]] = True
    #                 if curpos == destination:
    #                     return True
    #                 else:
    #                     l, r, u, d = curpos[1]-1, curpos[1]+1, curpos[0]-1, curpos[0]+1
    #                     while l >= 0 and not maze[curpos[0]][l]:
    #                         l -= 1
    #                     self.nodeque.append((curpos[0], l+1))
    #                     while r < self.n and not maze[curpos[0]][r]:
    #                         r += 1
    #                     self.nodeque.append((curpos[0], r-1))
    #                     while u >= 0 and not maze[u][curpos[1]]:
    #                         u -= 1
    #                     self.nodeque.append((u+1, curpos[1]))
    #                     while d < self.m and not maze[d][curpos[1]]:
    #                         d += 1
    #                     self.nodeque.append((d-1, curpos[1]))
    #     return False
                        
    def bfs(self, maze, start, destination):
        while self.nodeque:
            curpos = self.nodeque.popleft()

            if self.visited[curpos[0]][curpos[1]]:
                continue
            else:
                self.visited[curpos[0]][curpos[1]] = True
                if curpos == destination:
                    return True
                else:
                    l, r, u, d = curpos[1]-1, curpos[1]+1, curpos[0]-1, curpos[0]+1
                    while l >= 0 and not maze[curpos[0]][l]:
                        l -= 1
                    self.nodeque.append((curpos[0], l+1))
                    while r < self.n and not maze[curpos[0]][r]:
                        r += 1
                    self.nodeque.append((curpos[0], r-1))
                    while u >= 0 and not maze[u][curpos[1]]:
                        u -= 1
                    self.nodeque.append((u+1, curpos[1]))
                    while d < self.m and not maze[d][curpos[1]]:
                        d += 1
                    self.nodeque.append((d-1, curpos[1]))
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
print(s.hasPath(maze, (0,4), (3,2)))
#print(s.hasPath(canmaze, (0,4), (4,4)))






