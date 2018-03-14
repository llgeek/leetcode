class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letterval = []
        for word in words:
            val = 0
            for c in word:
                val |= 1 << (ord(c) - ord('a'))
            letterval.append(val)
        if not letterval or len(letterval) == 1:
            return 0
        maxproduct = 0
        for i in range(len(letterval)):
            for j in range(len(letterval)):
                maxproduct = len(words[i])*len(words[j]) \
                                if not letterval[i] & letterval[j] and len(words[i]) * len(words[j]) > maxproduct \
                                else maxproduct
        return maxproduct

s = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(s.maxProduct(words))
                
                    
