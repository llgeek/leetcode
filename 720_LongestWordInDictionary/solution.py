class Solution:
    def longestWord(self, words: 'List[str]') -> 'str':
        def buildGraph(words):
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            wordset = set(words)
            graph = dict()
            for word in words:
                graph[word] = set()
                for c in alpha:
                    if word+c in wordset:
                        graph[word].add(word+c)
            return graph
        
        if not words:
            return ''
        words.sort(key = lambda x: (len(x), x))
        if len(words[0]) != 1:
            return ''
        len2idx = {}
        for idx, w in enumerate(words):
            if len(w) not in len2idx:
                len2idx[len(w)] = idx
        for w in words[::-1]:

        
        

