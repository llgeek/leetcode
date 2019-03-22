class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and not trust:
            return 1
        cand = set()
        wrong = set()
        for t in trust:
            if t[0] in cand:
                cand.discard(t[0])
            wrong.add(t[0])
            if t[1] not in wrong:
                cand.add(t[1])
        if not cand:
            return -1
        candcnt = {}
        for c in cand:
            candcnt[c] = 0
        for t in trust:
            if t[1] in cand:
                candcnt[t[1]] += 1
                if candcnt[t[1]] == N-1:
                    return t[1]
        return -1
