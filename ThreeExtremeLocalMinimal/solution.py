# Complete the find_minima function below.
def find_minima(n, m):
    def next_unvisited(visited):
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    return (i, j)
        return (-1, -1)

    def update_minmal(x, localmin):
        if x < localmin[0]:
            localmin[2] = localmin[1]
            localmin[1] = localmin[0]
            localmin[0] = x
        elif x < localmin[1]:
            localmin[2] = localmin[1]
            localmin[1] = x
        elif x < localmin[2]:
            localmin[2] = x

    def DFS_visit(xid, yid):
        visited[xid][yid] = True
        islocalmin = True
        for d in distance:
            nebx, neby = xid + d[0], yid + d[1]
            if nebx < 0 or nebx >= n or neby < 0 or neby >= n:
                continue
            if not visited[nebx][neby] and m[nebx][neby] < m[xid][yid]:
                DFS_visit(nebx, neby)
                islocalmin = False
        if islocalmin:
            if is_local_mima(xid, yid):
                update_minmal(m[xid][yid], localmin)

    def is_local_mima(xid, yid):
        for d in distance:
            nebx, neby = xid + d[0], yid + d[1]
            if nebx < 0 or nebx >= n or neby < 0 or neby >= n:
                continue
            if m[nebx][neby] <= m[xid][yid]:
                return False
        return True

    #brute force way
    # min1, min2, min3 = (1<<31)-1, (1<<31)-1, (1<<31)-1
    # localmin = [min1, min2, min3]
    # distance = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    # for xid in range(n):
    #     for yid in range(n):
    #         if is_local_mima(xid, yid):
    #             update_minmal(m[xid][yid], localmin)
    # # if all(map(lambda x: x == (1<<31)-1, localmin)):
    # #     return []
    # # else:
    # return [mima for mima in localmin if mima != (1<<31)-1]

    visited = [[False] * n for _ in range(n)]
    min1, min2, min3 = (1 << 31)-1, (1 << 31)-1, (1 << 31)-1
    localmin = [min1, min2, min3]
    distance = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    xid, yid = next_unvisited(visited)
    while xid != -1 and yid != -1:
        DFS_visit(xid, yid)
        xid, yid = next_unvisited(visited)
    return [mima for mima in localmin if mima != (1 << 31)-1]
