"""
second trial

Union Find solution
"""


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return 
        m, n = len(board), len(board[0])
        ufhelper = UnionFind(m*n+1)
        distance = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j== 0 or j == n-1) and board[i][j] == 'O':
                    ufhelper.union(i*n+j, m*n)
                elif board[i][j] == 'O':
                    for d in distance:
                        nebx, neby = i + d[0], j + d[1]
                        if 0 <= nebx < m and 0 <= neby < n and board[nebx][neby] == 'O':
                            ufhelper.union(nebx * n + neby, i*n+j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and ufhelper.find(i*n+j) != ufhelper.find(m*n):
                    board[i][j] = 'X'


class UnionFind:
    def __init__(self, N):
        self.parents = [-1] * N
        for i in range(N):
            self.parents[i] = i 
        
    def find(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        node1p = self.find(node1)
        node2p = self.find(node2)
        if node1p != node2p:
            self.parents[node2p] = node1p