from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct_graph(wordList):
            graph = dict()
            for word in wordList:
                for i in range(len(word)):
                    newword = word[0:i] + '_' + word[i+1:]
                    graph[newword] = graph.get(newword, []) + [word]
            return graph

        graph = construct_graph(wordList)
        queue = deque()
        visited = set()
        queue.append((beginWord, 1))
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            visited.add(word)
            for i in range(len(word)):
                nebword = word[0:i] + '_' + word[i+1:]
                if nebword in graph:
                    for nword in graph[nebword]:
                        if nword not in visited:
                            queue.append((nword, depth+1))
        return 0
            

if __name__ == "__main__":
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "dog"]
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
