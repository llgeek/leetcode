"""
DFS with backtracking
"""
class Solution:
    def crackSafe(self, n, k):
        self.goalnum = k**n
        self.visited = set()
        self.result = ['0'] * n
        self.visited.add('0'*n)
        self.n = n
        self.k = k
        self.dfs()
        return ''.join(self.result)


    def dfs(self):
        if len(self.visited) == self.goalnum:
            return True
        prefix = ''.join(self.result[-self.n-1:] if self.n > 1 else '')
        for i in range(self.k):
            prefixstr = prefix + str(i)
            if prefixstr not in self.visited:
                self.visited.add(prefixstr)
                self.result.append(str(i))
                if self.dfs():
                    return True
                else:
                    self.visited.discard(prefixstr)
                    del self.result[-1]
        return False


s = Solution()
print(s.crackSafe(1, 2))
