class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def calc_f(s):
            if not s:
                return 0
            cc, cnt = s[0], 1
            for c in s[1:]:
                if c < cc:
                    cc = c
                    cnt = 1
                elif c == cc:
                    cnt += 1
            return cnt
        
        wordcnt = sorted(list(map(calc_f, words)), reverse=True)
        querycnt = list(map(calc_f, queries))
        res = []
        for qc in querycnt:
            val = 0
            for wc in wordcnt:
                if wc <= qc:
                    break
                val += 1
            res.append(val)
        return res
