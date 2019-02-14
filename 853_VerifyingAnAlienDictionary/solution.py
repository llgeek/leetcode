class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderdict = dict(zip(order, 'abcdefghijklmnopqrstuvwxyz'))
        pre = None
        for word in words:
            word = ''.join([orderdict[c] for c in word])
            if pre and pre > word:
                return False
            pre = word
        return True
        
if __name__ == "__main__":
    words = ["word", "world", "row"] 
    order = "worldabcefghijkmnpqstuvxyz"
    sol = Solution()
    print(sol.isAlienSorted(words, order))
