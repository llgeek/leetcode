class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        lastreached = {(r,c)}
        prevprob = [[0 for _ in range(N)] for _ in range(N)]
        prevprob[r][c] = 1.0
        for _ in range(K):
            curprob = [[0 for _ in range(N)] for _ in range(N)]
            curreached = set()
            for startpoint in lastreached:
                x, y = startpoint[0], startpoint[1]
                for nx, ny in zip([x+1, x+1, x-1, x-1, x+2, x+2, x-2, x-2], [y+2, y-2, y+2, y-2, y+1, y-1, y+1, y-1]):
                    if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                        continue
                    curprob[nx][ny] += 1/8 * prevprob[x][y]
                    curreached.add((nx, ny))
            prevprob = curprob
            lastreached = curreached
        return sum([prevprob[x][y] for x,y in lastreached])
    

if __name__ == '__main__':
    N = 3
    K = 2
    r = 0
    c = 0
    print(Solution().knightProbability(N, K, r, c))
