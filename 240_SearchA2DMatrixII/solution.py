"""
BFS idea

TLE in 

need to be optimized
"""


from collections import deque
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not any(matrix):
            return False
        distance = {(1,0), (-1, 0), (0, 1),  (0, -1)}
        visited = set()
        queue = deque()
        queue.append((0,0,matrix[0][0]))
        visited.add((0,0))
        while queue:
            nextlevel = deque()
            while queue:
                x, y, val = queue.popleft()
                visited.add((x,y))
                if val == target:
                    return True
                for d in distance:
                    nebx, neby = x+d[0], y+d[1]
                    if nebx < 0 or nebx >= len(matrix) or neby < 0 or neby >= len(matrix[0]) or matrix[nebx][neby] > target or (nebx, neby) in visited:
                        continue
                    nextlevel.append((nebx, neby, matrix[nebx][neby]))
            queue = nextlevel.copy()
        return False

if __name__ == "__main__":
    # matrix = [
    #     [1,   4,  7, 11, 15],
    #     [2,   5,  8, 12, 19],
    #     [3,   6,  9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    # target = 23
    matrix = [[-1], [-1]]
    target = -2
    sol = Solution()
    print(sol.searchMatrix(matrix, target))

