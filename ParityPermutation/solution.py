class Solution():
    def parityPermutation(self, n):
        """
        type n: int
        rtype: list[list] of int
        """
        def parityHelper(odds, evens, res, ifeven):
            choose = evens if ifeven else odds
            nextchoose = odds if ifeven else evens
            for tmpres in res:
                for num in choose:
                    tmpres += num
                    
        odds = [i for i in range(2, n+1,2)]
        evens = [i for i in range(1, n+1, 2)]
        res = [[]]
        
