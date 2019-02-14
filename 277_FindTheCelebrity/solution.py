class Solution():
    def findCelebrity(self, n):
        """ 
        type n: int
        rtype: int
        """
        candidatepossible = [True] * n
        for i in range(n):
            if not candidatepossible[i]:
                continue
            for j in range(n):
                jknowi = knows(j, i)
                iknowj = knows(i, j)
                if i != j and (not jknowi or iknowj):
                    candidatepossible[i] = False
                    break
                elif i != j and (jknowi or not iknowj):
                    candidatepossible[j] = False
            if candidatepossible[i]:
                return i 
        return -1
