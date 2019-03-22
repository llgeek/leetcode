class Solution:
    def buildGraph(self, words):
        self.graph = {}
        self.indegree = {}
        for word in words:
            for c in word:
                self.indegree[c] = 0
        
        for i in range(1, len(words)):
            k = 0
            minlen = min(len(words[i-1]), len(words[i]))
            while k < minlen and words[i-1][k] == words[i][k]:
                k += 1
            if k < minlen:
                self.indegree[words[i][k]] += 1
                self.graph[words[i-1][k]] = self.graph.get(words[i-1][k], set()) | {words[i][k]}
            if k < len(words[i-1]) and k == len(words[i]):
                raise RuntimeError


    def allienOrder(self, words):
        if not words:
            return ''
        try:
            self.buildGraph(words)
        except RuntimeError:
            return ''
        res = []
        stack = []
        for c, degree in self.indegree.items():
            if degree == 0:
                stack.append(c)
        while stack:
            node = stack.pop()
            res.append(node)
            for nebnode in self.graph.get(node, set()):
                self.indegree[nebnode] -= 1
                if self.indegree[nebnode] == 0:
                    stack.append(nebnode)
        return '' if len(res) != len(self.indegree.keys()) else ''.join(res)

if __name__ == "__main__":
    # words = [
    #     "wrt",
    #     "wrf",
    #     "er",
    #     "ett",
    #     "rftt"
    # ]
    # words = [
    #     "z",
    #     "x"
    # ]
    words = [
        "z",
        "x",
        "z"
    ]
    sol = Solution()
    print(sol.allienOrder(words))
        
