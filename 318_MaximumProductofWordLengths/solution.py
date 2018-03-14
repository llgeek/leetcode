 
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter2len = dict()
        for word in words:
            if not word:
                continue
            n = len(word)
            letters = ''.join(sorted(set(word)))
            if letter2len.get(letters, 0) < n:
                letter2len[letters] = n
        if not letter2len or len(letter2len) == 1:
            return 0
        products = [x*y for kx, x in letter2len.items()
                    for ky, y in letter2len.items() if not set(kx).intersection(set(ky))]
        return 0 if not products else max(products)


s = Solution()

words = ["abc"
         "a"
         ""]

print(s.maxProduct(words))
