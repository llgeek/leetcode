from collections import deque, defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def buildGraph(wordList, beginWord):
            wordset = set(wordList)
            graph = defaultdict(lambda : [])
            for word in wordList + ([beginWord] if beginWord not in wordset else []):
                for idx, c in enumerate(word):
                    for nc in alp:
                        if nc != c:
                            newword = word[0:idx] + nc + word[idx+1:]
                            if newword in wordset:
                                graph[word].append(newword)
            return graph
        
        alp = 'abcdefghijklmnopqrstuvwxyz'
        graph = buildGraph(wordList, beginWord)
        visited = set()
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, depth = queue.popleft()
            visited.add(word)
            if word == endWord:
                return depth
            for nebword in graph[word]:
                if nebword not in visited:
                    queue.append((nebword, depth+1))
        return 0

if __name__ == "__main__":
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ["hot","dot","dog","lot","log","cog"]
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "dog"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
