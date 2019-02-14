class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        banned = set(banned)
        tmpword = []
        words = []
        for c in paragraph:
            if c in "!?',;. ":
                word = ''.join(tmpword).lower()
                if word in banned:
                    tmpword = []
                    continue
                if word:
                    words.append(word)
                    tmpword = []
            else:
                tmpword.append(c)
        word = ''.join(tmpword).lower()
        if word and word not in banned:
            words.append(word)
        return Counter(words).most_common(1)[0][0]

if __name__ == "__main__":
    paragraph = 'Bob'
    banned = []
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
        

