class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def buildgraph(beginWord, wordList):
            wordset = set(wordList)
            graph = {}
            