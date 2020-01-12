class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def fn(word):
            if not word: return 0
            res, c = 1, word[0]
            for cc in word[1:]:
                if cc < c:
                    res, c = 1, cc
                elif c == cc:
                    res += 1
            return res
        
        queries_freq = [fn(q) for q in queries]
        words_freq = [fn(w) for w in words]
        return [sum(q < w for w in words_freq) for q in queries_freq]

