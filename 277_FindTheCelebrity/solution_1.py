
class Solution:
    def knows(self, a, b):
        """
        second trial

        helper function
        
        tells you whether A knows B.
        """
        pass

    def findCelebrity(self, n):
        celebrity = [True] * n
        for i in range(n):
            if celebrity[i]:
                for j in range(n):
                    if i != j:
                        jknowi = knows(j, i)
                        iknowj = knows(i, j)
                        if jknowi or not iknowj:
                            celebrity[j] = False
                        if iknowj or not jknowi:
                            celebrity[i] = False
                            break
                if celebrity[i]:
                    return i
        return -1

