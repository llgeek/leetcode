class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def findOnesIndex():
            for i in range(m):
                if A[i][0]:
                    return (i, 0)
                if A[i][n-1]:
                    return (i, n-1)
            for i in range(n):
                if A[0][i]:
                    return (0, i)
                if A[m-1][i]:
                    return (m-1, i)
            return (-1, -1)

        def dfs(x, y):
            dist = {(0, 1), (0, -1), (-1, 0), (1, 0)}
            A[x][y] = 0
            for d in dist:
                nebx, neby = x + d[0], y + d[1]
                if 0 <= nebx < m and 0 <= neby < n and A[nebx][neby]:
                    dfs(nebx, neby)
        if not any(A):
            return 0
        m, n = len(A), len(A[0])
        while True:
            x, y = findOnesIndex()
            if x == -1:
                break
            dfs(x, y)
        return sum(map(sum, A))
