class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def build_graph(wordset):
            graph = {}
            for word in wordset:
                graph[word] = set()
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        neb = word[:i] + c + word[i+1:]
                        if neb in wordset:
                            graph[word].add(neb)
            return graph
        
        def bfs(graph, s, t):
            visited = {s}
            queue = [s]
            dist = 0
            while queue:
                nextlevel = []
                dist += 1
                while queue:
                    node = queue.pop()
                    if node == t:
                        return dist
                    for neb in graph[node]:
                        if neb not in visited:
                            visited.add(neb)
                            nextlevel.append(neb)
                queue = nextlevel[:]
            return 0


        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        graph = build_graph(wordset | {beginWord, endWord})
        return bfs(graph, beginWord, endWord)

