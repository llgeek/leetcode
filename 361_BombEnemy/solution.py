class Solution(object):
    def bombEnemy(self, grid):
        """ 
        type grid: list of list, 'E' represents enemy, 'W' represents wall, 0 represents empty cell
        trype: int, number of enemies you can kill
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res, rowEnum, colEnum = 0, 0, [0]*n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rowEnum = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        rowEnum += 1 if grid[i][k] == 'E' else 0
                if i == 0 or grid[i-1][j] == 'W':
                    colEnum[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        colEnum[j] += 1 if grid[k][j] == 'E' else 0
                if grid[i][j] == '0':
                    res = max(res, rowEnum + colEnum[j])
        return res

grid = [
    ['0', 'E', '0', '0'],
    ['E', '0', 'W', 'E'],
    ['0', 'E', '0', '0']
]

s = Solution()
print(s.bombEnemy(grid))
                        
                
