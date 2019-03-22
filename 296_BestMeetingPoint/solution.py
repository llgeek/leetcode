"""
for 1D, the meeting point is the median point

because of Manhattan distance, 2D can be seperated solved on X and Y axis
"""

class Solution:
    def meetingPoint(self, grid):
        if not any(grid):
            return 0
        X, Y = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    X.append(i)
                    Y.append(j)
        X.sort()
        Y.sort()
        ans = 0
        i, j = 0, len(X)-1
        while i < j:
            ans += (X[j] - X[i])
            ans += (Y[j] - Y[i])
            i += 1
            j -= 1
        return ans